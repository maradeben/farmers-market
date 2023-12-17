from mongoengine import connect, disconnect,\
        DynamicDocument, IntField, StringField, ReferenceField, DateTimeField, FloatField, EmailField,\
            ListField
from mongoengine.errors import NotUniqueError
from pymongo.errors import DuplicateKeyError
import datetime
from os import environ


class DB_Store:
    _instance = None
    db_name = environ.get('DB_NAME', 'fm_exp')
    host = environ.get('HOST', '127.0.0.1')
    port = int(environ.get('PORT', '27017'))
    meta = {'db_alias': 'test'}

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DB_Store, cls).__new__(cls)
            cls._instance.connect()
        return cls._instance
    
    @classmethod
    def connect(cls):
        connect('fm_exp', host=cls.host, port=cls.port)

    @classmethod
    def close_connection(cls):
        disconnect('test')


engine = DB_Store()
# engine.connect()
# connect('fm_exp')



class Vendor(DynamicDocument):
    phone = StringField(required=True)
    email = EmailField(required=True, unique=True)
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    username = StringField(required=True)
    farmname = StringField(required=True)
    location = StringField(required=True)
    rating = FloatField(required=True)
    password = StringField(required=True)
    created_at = DateTimeField(required=True, default=datetime.datetime.now())

    meta = {
        'collection': 'vendors'
    }
    # override init function to accomodate auto-saving on creation
    def __init__(self, **kwargs):
        # default init to create the object
        super(Vendor, self).__init__(**kwargs)
        self.save()


class DuplicateProductError(Exception):
    """ custom exception for duplicate product """
    def __init__(self, message="Duplicate product"):
        self.message = message
        super().__init__(self.message)


# function to create and save product
def product_create_save(**kwargs):
    """ bundle creation and saving of product """
    product = Product(**kwargs)
    is_existing = False

    try:
        is_existing = product.exists(product.name, product.category, product.vendor, product.stock)
    except DuplicateProductError as e:
        print("Product error:", e)
    if not is_existing:
        product.save()
        return product

class Product(DynamicDocument):
    name = StringField(required=True)
    price = FloatField(required=True)
    unit = StringField(required=True)
    category = StringField(required=True)
    stock = IntField(required=True)
    vendor = ReferenceField(Vendor, required=True)
    rating = FloatField(required=True)
    num_ratings = IntField(required=True, default=0)
    image_url = ListField(StringField(), required=True,
            default=['frontend/assets/images/product-images/default-product-image.jpg'])
    
    meta = {
        'collection': 'products'
    }


    # override init function to accomodate auto-saving on creation
    def __init__(self, **kwargs):
        # default init to create the object
        super(Product, self).__init__(**kwargs)
        # self.save()
    
    def exists(self, name, category, vendor, stock):
        """ if product exists, raise exception, if not, return False """
        existing_product = Product.objects(name=name, category=category, vendor=vendor, stock=stock)
        if existing_product:
            raise DuplicateProductError(message="This product exists")
        return False

try:
    vendor1 = Vendor(
        **{
        "rating": 3.0,
        "num_ratings": 0,
        "phone": "018-810",
        "email": "wisdom@mailer.com",
        "firstname": "Wisdom",
        "lastname": "Greens",
        "username": "GreenFarms",
        "farmname": "Green Farms",
        "location": "Gombe",
        "password": "abc"
        }
    )

    vendor2 = Vendor(
        **{
            "rating": 5.0,
            "num_ratings": 0,
            "phone": "182-233",
            "email": "georgeamara@ymail.com",
            "firstname": "Amara",
            "lastname": "Goerge",
            "username": "amaregeorge",
            "farmname": "Animal Farm",
            "location": "Suleja",
            "password": "abc"
        }
    )

except (DuplicateKeyError, NotUniqueError):
    print('Vendor profile exists')

product1 = product_create_save(
    **{
        "name": "Cocoa",
        "category": "Roots/Tubers",
        "unit": "unit",
        "vendor": Vendor.objects(email='wisdom@mailer.com').first(),
        "num_ratings": 0,
        "image_url": ["frontend/assets/images/product-images/default-product-image.jpg"],
        "object": "Product",
        "price": 1695,
        "stock": 253,
        "rating": 5.0
    }
)

product2 = product_create_save(
    **{
        "name": "Beetroot",
        "category": "Roots/Tubers",
        "unit": "unit",
        "vendor": Vendor.objects(email='georgeamara@ymail.com').first(),
        "num_ratings": 0,
        "image_url": ["frontend/assets/images/product-images/default-product-image.jpg"],
        "price": 1614,
        "stock": 748,
        "rating": 4.0
    }
)

print(product1.vendor)

engine.close_connection()
