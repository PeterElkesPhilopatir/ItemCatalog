from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item
import string, random

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import facebook

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
database_session = DBSession()


@app.route('/gconnect', methods=['POST'])
def gconnect():
    if (login_session['state'] == None):  # validate user state
        code = request.data  # get the code
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='', redirect_uri='postmessage')

        credentials = oauth_flow.step2_exchange(code)
        access_token = credentials.access_token
        url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
               % access_token)

        print (url)
        # request with google server to authenticate the code
        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1])
        # print result

        if result.get('error') is not None:
            response = make_response(json.dumps(result.get('error')), 500)
            response.headers['Content-Type'] = 'application/json'
            print "errorrrrrrr!!!!!!!!!!"
            return response
        gplus_id = credentials.id_token['sub']

        if result['user_id'] != gplus_id:
            response = make_response(
                json.dumps("Token's user ID doesn't match given user ID."), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        # the code is authenticated now fetch user data

        userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        params = {'access_token': credentials.access_token, 'alt': 'json'}
        answer = requests.get(userinfo_url, params=params)
        data = answer.json()

        login_session['state'] = data['email']
        print ('state' + login_session['state'])
        login_session['username'] = data['name']
        id = int(data['id'])
        login_session['id'] = id % 1000
        login_session['access_token'] = access_token
        login_session['provider'] = 'google'

        return redirect(url_for('showCategories'))
    else:
        return "You already logged in "


@app.route('/fbconnect', methods=['POST'])
def fbconnet():
    # if login_session['state'] == None:  # validate user state
    access_token = request.data  # get access token from client

    # authenticate with facebook server this token
    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)

    print "URL>>" + url
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # now token is authenticated
    token = result['access_token']  # after validation

    # get user data using graph request
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me')
    args = {'fields': 'id,name,email', }
    profile = graph.get_object('me', **args)
    # login_session['state'] = profile['email']
    login_session['username'] = profile['name']
    id = int(profile['id'])
    login_session['id'] = id % 1000
    login_session['provider'] = 'facebook'
    login_session['access_token'] = access_token
    print "access>>" + access_token
    print "name>>" + login_session['username']

    return redirect(url_for('showCategories'))

    # session['username'] = data["name"]
    # session['state'] = data["email"]


@app.route('/category/<int:category_id>/menu/JSON')
def categoryMenuJSON(category_id):
    category = database_session.query(Category).filter_by(id=category_id).one()
    items = database_session.query(Item).filter_by(
        category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/category/<int:category_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(category_id, menu_id):
    Menu_Item = database_session.query(Item).filter_by(id=menu_id).one()
    return jsonify(Menu_Item=Menu_Item.serialize)


@app.route('/category/JSON')
def categoriesJSON():
    categories = database_session.query(Category).all()
    return jsonify(categories=[r.serialize for r in categories])


# Create anti-forgery state token
# @app.route('/login')
# def login():
#     state = ''.join(random.choice  (string.ascii_uppercase + string.digits)
#                     for x in xrange(32))
#     login_session['state'] = state
#     # return "The current session state is %s" % login_session['state']
#     return render_template('login.html',STATE = state)

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    if request.method == 'POST':
        if login_session['provider'] == 'facebook' and database_session['state'] is not None:
            access_token = login_session['access_token']
            facebook_id = login_session['id']
            # logout user from facebook
            url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id, access_token)
            h = httplib2.Http()
            result = h.request(url, 'DELETE')[1]
            # delete user session
            del login_session['state']
            del login_session['username']
            del login_session['access_token']
            del login_session['id']


        elif login_session['provider'] == 'google' and login_session['state'] is not None:
            access_token = login_session['access_token']
            # logout user from google
            url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
            h = httplib2.Http()
            result = h.request(url, 'GET')[0]
            # delete user session and logout user from menu item app
            del login_session['state']
            del login_session['username']
            del login_session['access_token']
            del login_session['id']

        return redirect(url_for('showCategories'))


# Show all categories
@app.route('/')
@app.route('/category/')
def showCategories():
    if 'state' not in login_session:  # init all session with none values
        login_session['state'] = None
    if 'username' not in login_session:
        login_session['username'] = None
    if 'id' not in login_session:
        login_session['id'] = None

    categories = database_session.query(Category).all()
    # return "This page will show all my categories"
    # print "size >> "+str(len(categories))
    return render_template('categories.html', categories=categories)


# Create a new category
@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        if login_session['state'] is not None:
            uid = login_session['id']
            newCategory = Category(user_id=uid, name=request.form['name'])
            database_session.add(newCategory)
            database_session.commit()
            return redirect(url_for('showCategories'))
        else:
            print "unauthorized"
            return redirect(url_for('showCategories'))

    else:

        return render_template('newCategory.html')
        # return "This page will be for making a new category"


# Edit a category
@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = database_session.query(Category).filter_by(id=category_id).one()

    if request.method == 'POST':
        if login_session['state'] is not None:
            if editedCategory.user_id == login_session['id']:
                if request.form['name']:
                    editedCategory.name = request.form['name']
                    return redirect(url_for('showCategories'))
            else:
                return render_template('editCategory.html', category=editedCategory)
    else:
        print "unauthorized"

        return render_template(
            'editCategory.html', category=editedCategory)

        # return 'This page will be for editing category %s' % category_id


# Delete a category
@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = database_session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if login_session['state'] is not None:
            if categoryToDelete.user_id == login_session['id']:
                database_session.delete(categoryToDelete)

                itemsToDelete = database_session.query(Item).filter_by(category_id=category_id).one()
                database_session.delete(itemsToDelete)

                database_session.commit()

                return redirect(url_for('showCategories', category_id=category_id))
            else:
                print "unauthorized"

                return redirect(url_for('showCategories', category_id=category_id))
    else:
        return render_template(
            'deleteCategory.html', category=categoryToDelete)
        # return 'This page will be for deleting category %s' % category_id


# Show a category menu
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/menu/')
def showMenu(category_id):
    category = database_session.query(Category).filter_by(id=category_id).one()
    items = database_session.query(Item).filter_by(category_id=category_id).all()
    return render_template('menu.html', items=items, category=category)
    # return 'This page is the menu for category %s' % category_id


# Create a new menu item
@app.route('/category/<int:category_id>/menu/new/', methods=['GET', 'POST'])
def newItem(category_id):
    if request.method == 'POST':
        get_category = database_session.query(Category).filter_by(id=category_id).one()
        if login_session['state'] is not None:
            if get_category.user_id == login_session['id']:
                newItem = Item(user_id=login_session['id'],name=request.form['name'], description=request.form[
                    'description'], price=request.form['price'], course=request.form['course'], category_id=category_id)
                database_session.add(newItem)
                database_session.commit()
                return redirect(url_for('showMenu', category_id=category_id))
            else:
                return redirect(url_for('showMenu', category_id=category_id))

        else:
            print "unauthorized"

            return "you should log in to create item"
    else:
        return render_template('newitem.html', category_id=category_id)

        # return 'This page is for making a new menu item for category %s'
        # %category_id


# Edit a menu item
@app.route('/category/<int:category_id>/menu/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editItem(category_id, menu_id):
    editedItem = database_session.query(Item).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if editedItem.user_id == login_session['id']:
            if request.form['name']:
                editedItem.name = request.form['name']
            if request.form['description']:
                editedItem.description = request.form['name']
            if request.form['price']:
                editedItem.price = request.form['price']
            if request.form['course']:
                editedItem.course = request.form['course']
            database_session.add(editedItem)
            database_session.commit()
            return redirect(url_for('showMenu', category_id=category_id))
        else:
            print "unauthorized"

            return redirect(url_for('showMenu', category_id=category_id))
    else:
        return render_template('edititem.html', category_id=category_id, menu_id=menu_id, item=editedItem)

        # return 'This page is for editing menu item %s' % menu_id


# Delete a menu item
@app.route('/category/<int:category_id>/menu/<int:menu_id>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_id, menu_id):
    itemToDelete = database_session.query(Item).filter_by(id=menu_id).one()
    if request.method == 'POST':
        print'itemUserID>>'+str(itemToDelete.user_id) +'session'+str(login_session['id'])
        if itemToDelete.user_id == login_session['id']:
            database_session.delete(itemToDelete)
            database_session.commit()
            return redirect(url_for('showMenu', category_id=category_id))
        else:
            print "unauthorized"
            return redirect(url_for('showMenu', category_id=category_id))
    else:
        return render_template('deleteItem.html', item=itemToDelete)
        # return "This page is for deleting menu item %s" % menu_id


if __name__ == '__main__':
    app.secret_key = 'peter super key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
