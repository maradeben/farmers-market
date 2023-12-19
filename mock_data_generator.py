from backend.models.vendor import register_vendor, Vendor
from backend.models.user import register_user
from backend.models.product import register_product
from backend.database.db_storage import storage_engine
from backend.models.utils import hash_password
from mongoengine.errors import NotUniqueError
from pymongo.errors import DuplicateKeyError

from backend.custom_errors import *

import mongoengine
import random
random.seed(42)


mongoengine.disconnect('core')
storage_engine.close_connection()
storage_engine.connect()

## some mock data
phones = ['123-456', '232-185', '858-991', '111-111', '999-124', '893-903', '444-555', '692-804', '182-233', '018-810']

firstnames = ['Amos', 'Ilua', 'Bukola', 'Chinonso', 'Ephraim', 'Iyabode', 'Hamida', 'Kingsley', 'Amara', 'Wisdom', 'Ogbonna',\
                'Akpan', 'Ibrahim', 'Suliat', 'Idris', 'Ciroma', 'Yoanna', 'Simbi', 'Idris', 'Glob', 'Matthew', 'Shuga',\
                    'Olusegun', 'Amadilo', 'Tunbi', 'Johsnon', 'Faith', 'Peace', 'Olaide', 'Gift']
lastnames = ['Goodwill', 'Bilunde', 'Johnson', 'Akpan', 'Manasseh', 'Oludairo', 'Ahmad', 'Contan', 'Goerge', 'Greens', 'Godwin',\
                'Baba', 'Muhammad', 'Olaifa', 'Adamu', 'Chukwuma', 'Justin', 'Atah', 'Ondase', 'Bob', 'Luke', 'Honda',\
                    'Oladale', 'Leprang', 'Agagu', 'Ibeh', 'Idris', 'Charity', 'Adedeji', 'Kehinde']
emails = ['amosgoodwill@ymail.com', 'bilua@starfarms.com', 'johnbull@ymail.com', 'chiakpan@fresh.com', 'ephman@cabmail.com',\
            'iyabodairo@cabmail.com', 'ahmad.h@coldmail.com', 'c.kingsley@kingsplace.com', 'georgeamara@ymail.com', 'wisdom@mailer.com',\
                'ogboy@ymail.com', 'baba@mymail.com', 'mubi@amail.com', 'suliatifa@cabmail.com', 'adams_id@mail.com', 'ceesxy232@mail.com',\
                    'yojustin@ymail.com', 'atam1998@cabmail.com', 'ondase112@ymail.com', 'globob@mail.com', 'disciple@ymail.com',\
                        'hondaman22@cabmail.com', 'olasegum@mail.com', 'amadilo.lebrang@ymail.com', 'ogaagagu@mail.com', 'chukwujohnson@mail.com',\
                            'idrisfatih@maloo.com', 'chartiyispeace@cabmail.com', 'olaideade@mail.com', 'kehinde.gift@ymail.com']

usernames = ['amogood', 'star_farmer', 'johns_b', 'apk_chi', 'theman', 'iyadairo', 'amida', 'kings', 'amaregeorge', 'GreenFarms']
farmnames = ['Amos Farm', 'Star Farms', 'Johhny JC', 'Chi Fresh Produce', 'Ephraim&Manasseh', 'Dairo Poultry', \
                'Amida Farm', 'Kings Place', 'Animal Farm', 'Green Farms']
locations = ['Abuja', 'Kogi', 'Ilorin', 'Ibadan', 'Nsukka', 'Benin', 'Otukpo', 'Ijebu', 'Suleja', 'Gombe']


# generate mock user data
mocked_users = []

for email, first, last in zip(emails, firstnames, lastnames):
    try:
        user = register_user(
            **{
                "email": email,
                "firstname": first,
                "lastname": last,
                "password": hash_password("abc")
            }
        )
    except (DuplicateKeyError, NotUniqueError, DuplicateVendorError, DuplicateUserError):
        continue
    mocked_users.append(user)


# generate mock vendor data
vendors = []
for email,loc, farm in zip(emails[:10], locations[:10], farmnames[:10]):
    rating = float(random.randint(3,5))
    try:
        vendor = register_vendor(
            **{
                "email": email,
                "farmname": farm,
                "location": loc
            }
        )
    except (DuplicateKeyError, NotUniqueError, UserNotFoundError):
        continue

    vendors.append(vendor)


# generate mock products
products = []
cats = {
    "Roots/Tubers": ['Yam', 'Cocoa', 'Carrot', 'Potatoe', 'Cassava', 'Ginger', 'Turmeric', 'Turnip', 'Beetroot', 'Groundnut'],
    "Fruits/Vegetables": ['Apple', 'Banana', 'Orange', 'Mango', 'Strawberry', 'Grapes', 'Avocado', 'Tomato', 'Watermelon', 'Peach',\
                            'Onion', 'Cucumber', 'Spinahch', 'Water leaf'],
    "Oils": ['Olive oil', 'Canola Oil', 'Sunflower oil', "Corn oil", "Peanut oil", 'Vegetable oil', 'Groundnut oil'],
    "Meat/Fish": ['Chicken', 'Beef', 'Pork', 'Lamb', 'Turkey', 'Duck', 'Vension', 'Eggs', 'Goat', 'Rabbit'],
    "Grains": ['Rice', 'Wheat', 'Corn', 'Barley', 'Oats', 'Millet', 'Rye']
}
image_urls = {
    "Roots/Tubers": "frontend/assets/images/product-images/roots-placeholder-image.png",
    "Fruits/Vegetables": "frontend/assets/images/product-images/vegetables-placeholder-image.png",
    "Oils": "frontend/assets/images/product-images/oil-placeholder-image.png",
    "Meat/Fish": "frontend/assets/images/product-images/meat-placeholder-image.png",
    "Grains": "frontend/assets/images/product-images/grains-placeholder-image.png"
}

for i in range(500):
    cat = random.choice(list(cats.keys()))
    # print(cat)
    name = random.choice(cats[cat])
    if cat == 'Roots/Tubers' or cat == 'Fruits/Vegetables':
        price = random.randrange(800, 3000)
        unit = 'unit'
    elif cat == 'Oils':
        price = random.randrange(2000, 12000)
        unit = 'litre'
    elif cat == 'Meat/Poultry':
        price = random.randrange(2500, 15000)
        unit = 'kg'
    elif cat == 'Grain':
        price = random.randrange(8000, 85000)
        unit = 'bag'
    else:
        unit = "unit"
        price = 999
    stock = random.randrange(15, 1000)
    vendor = random.choice(vendors) # ids actually contain vendor objects
    rating = float(random.randint(3,5))
    
    # product = Product(name, cat, price, unit, stock, vendor_id, rating)
    product = register_product(
        **{
        "product_name": name,
        "category": cat,
        "unit": unit,
        "vendor": Vendor.objects(email=vendor.email).first(),
        "num_ratings": 0,
        "image_url": [image_urls[cat]],
        "price": price,
        "stock": stock,
        "rating": rating
    }
    )

    products.append(product.id)


storage_engine.close_connection()
