from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
category1 = Category(user_id=1, name="Urban Burger")

session.add(category1)
session.commit()

item2 = Item(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                 price="$7.50", course="Entree", category=category1)

session.add(item2)
session.commit()

item1 = Item(user_id=1, name="French Fries", description="with garlic and parmesan",
                 price="$2.99", course="Appetizer", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Chicken Burger",
                 description="Juicy grilled chicken patty with tomato mayo and lettuce",
                 price="$5.50", course="Entree", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Chocolate Cake", description="fresh baked and served with ice cream",
                 price="$3.99", course="Dessert", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Sirloin Burger", description="Made with grade A beef",
                 price="$7.99", course="Entree", category=category1)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Root Beer", description="16oz of refreshing goodness",
                 price="$1.99", course="Beverage", category=category1)

session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Iced Tea", description="with Lemon",
                 price="$.99", course="Beverage", category=category1)

session.add(item6)
session.commit()

item7 = Item(user_id=1, name="Grilled Cheese Sandwich",
                 description="On texas toast with American Cheese", price="$3.49", course="Entree",
                 category=category1)

session.add(item7)
session.commit()

item8 = Item(user_id=1, name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                 price="$5.99", course="Entree", category=category1)

session.add(item8)
session.commit()

# Menu for Super Stir Fry
category2 = Category(user_id=1, name="Super Stir Fry")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                 price="$7.99", course="Entree", category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Peking Duck",
                 description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook",
                 price="$25", course="Entree", category=category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Spicy Tuna Roll",
                 description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                 price="15", course="Entree", category=category2)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Nepali Momo ",
                 description="Steamed dumplings made with vegetables, spices and meat. ",
                 price="12", course="Entree", category=category2)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Beef Noodle Soup",
                 description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                 price="14", course="Entree", category=category2)

session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Ramen",
                 description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                 price="12", course="Entree", category=category2)

session.add(item6)
session.commit()

# Menu for Panda Garden
category1 = Category(user_id=1, name="Panda Garden")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Pho",
                 description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                 price="$8.99", course="Entree", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Chinese Dumplings",
                 description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                 price="$6.99", course="Appetizer", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Gyoza",
                 description="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",
                 price="$9.95", course="Entree", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Stinky Tofu",
                 description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                 price="$6.99", course="Entree", category=category1)

session.add(item4)
session.commit()

item2 = Item(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                 price="$9.50", course="Entree", category=category1)

session.add(item2)
session.commit()

# Menu for Thyme for that
category1 = Category(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Tres Leches Cake",
                 description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                 price="$2.99", course="Dessert", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                 price="$5.99", course="Entree", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Honey Boba Shaved Snow",
                 description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                 price="$4.50", course="Dessert", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Cauliflower Manchurian",
                 description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                 price="$6.95", course="Appetizer", category=category1)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Aloo Gobi Burrito",
                 description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                 price="$7.95", course="Entree", category=category1)

session.add(item5)
session.commit()

item2 = Item(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                 price="$6.80", course="Entree", category=category1)

session.add(item2)
session.commit()

# Menu for Tony's Bistro
category1 = Category(user_id=1, name="Tony\'s Bistro ")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Shellfish Tower",
                 description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                 price="$13.95", course="Entree", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Chicken and Rice", description="Chicken... and rice",
                 price="$4.95", course="Entree", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Mom's Spaghetti",
                 description="Spaghetti with some incredible tomato sauce made by mom",
                 price="$6.95", course="Entree", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                 description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course="Dessert",
                 category=category1)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Tonkatsu Ramen",
                 description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                 price="$7.95", course="Entree", category=category1)

session.add(item5)
session.commit()

# Menu for Andala's
category1 = Category(user_id=1, name="Andala\'s")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Lamb Curry",
                 description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                 price="$9.95", course="Entree", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                 price="$7.95", course="Entree", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Potstickers",
                 description="Delicious chicken and veggies encapsulated in fried dough.",
                 price="$6.50", course="Appetizer", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                 price="$6.75", course="Appetizer", category=category1)

session.add(item4)
session.commit()

item2 = Item(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                 price="$7.00", course="Entree", category=category1)

session.add(item2)
session.commit()

# Menu for Auntie Ann's
category1 = Category(user_id=1, name="Auntie Ann\'s Diner' ")

session.add(category1)
session.commit()

item9 = Item(user_id=1, name="Chicken Fried Steak",
                 description="Fresh battered sirloin steak fried and smothered with cream gravy", price="$8.99",
                 course="Entree", category=category1)

session.add(item9)
session.commit()

item1 = Item(user_id=1, name="Boysenberry Sorbet",
                 description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                 price="$2.99", course="Dessert", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Broiled salmon",
                 description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                 price="$10.95", course="Entree", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Morels on toast (seasonal)",
                 description="Wild morel mushrooms fried in butter, served on herbed toast slices", price="$7.50",
                 course="Appetizer", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Tandoori Chicken",
                 description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                 price="$8.95", course="Entree", category=category1)

session.add(item4)
session.commit()

item2 = Item(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                 price="$9.50", course="Entree", category=category1)

session.add(item2)
session.commit()

item10 = Item(user_id=1, name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                  price="$1.99", course="Dessert", category=category1)

session.add(item10)
session.commit()

# Menu for Cocina Y Amor
category1 = Category(user_id=1, name="Cocina Y Amor ")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Super Burrito Al Pastor",
                 description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price="$5.95",
                 course="Entree", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Cachapa",
                 description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                 price="$7.99", course="Entree", category=category1)

session.add(item2)
session.commit()

category1 = Category(user_id=1, name="State Bird Provisions")
session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Chantrelle Toast",
                 description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                 price="$5.95", course="Appetizer", category=category1)

session.add(item1)
session.commit

item1 = Item(user_id=1, name="Guanciale Chawanmushi",
                 description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)", price="$6.95",
                 course="Dessert", category=category1)

session.add(item1)
session.commit()

item1 = Item(user_id=1, name="Lemon Curd Ice Cream Sandwich",
                 description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                 price="$4.25", course="Dessert", category=category1)

session.add(item1)
session.commit()

print ("added menu items!")
