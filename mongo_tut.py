from mongoengine import connect, disconnect,\
        DynamicDocument, EmbeddedDocument, EmbeddedDocumentField, IntField, StringField, ReferenceField,\
            DateTimeField, FloatField, EmailField, ListField
from mongoengine.errors import NotUniqueError
from pymongo.errors import DuplicateKeyError
import datetime
from os import environ
import json


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
print(engine.db_name)
print(engine.__doc__)
# engine.connect()
# connect('fm_exp')

class User(DynamicDocument):
    phone = StringField()
    email = EmailField(required=True, unique=True)
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    username = StringField()
    password = StringField(required=True)
    role = StringField(default='user')
    cart = ListField(ListField())
    created_at = DateTimeField(required=True, default=datetime.datetime.now())

    meta = {
        'collection': 'users',
        "allow_inheritance": True
    }
    # # override init function to accomodate auto-saving on creation
    # def __init__(self, **kwargs):
    #     # default init to create the object
    #     super(Vendor, self).__init__(**kwargs)
    #     self.save()


class VendorInfo(EmbeddedDocument):
    """ Additional vendor specific details """
    farmname = StringField(required=True)
    location = StringField(required=True)
    rating = FloatField(default=0)
    num_ratings = IntField(default=0)
    


class Vendor(User):
    vendor_details = EmbeddedDocumentField(VendorInfo, required=True)
    role = StringField(default='vendor')

    # meta = {
    #     'collection': 'vendors'
    # }
    # # override init function to accomodate auto-saving on creation
    # def __init__(self, **kwargs):
    #     # default init to create the object
    #     super(Vendor, self).__init__(**kwargs)
    #     self.save()


class DuplicateProductError(Exception):
    """ custom exception for duplicate product """
    def __init__(self, message="Duplicate product"):
        self.message = message
        super().__init__(self.message)

class DuplicateUserError(Exception):
    """ custom exception for duplicate user """
    def __init__(self, message="User exists"):
        self.message = message
        super().__init__(self.message)

class DuplicateVendorError(Exception):
    """ custom exception for duplicate user """
    def __init__(self, message="Vendor exists"):
        self.message = message
        super().__init__(self.message)

class UserNotFoundError(Exception):
    """ custom exception for user not found """
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)



class Product(DynamicDocument):
    product_name = StringField(required=True)
    price = FloatField(required=True)
    unit = StringField(required=True)
    category = StringField(required=True)
    stock = IntField(required=True)
    vendor = ReferenceField(Vendor, required=True)
    rating = FloatField(required=True)
    num_ratings = IntField(required=True, default=0)
    image_url = ListField(StringField(), required=True,
            default=['frontend/assets/images/product-images/default-product-image.jpg'])
    created_at = DateTimeField(required=True, default=datetime.datetime.now())
    
    meta = {
        'collection': 'products'
    }


    # # override init function to accomodate auto-saving on creation
    # def __init__(self, **kwargs):
    #     # default init to create the object
    #     super(Product, self).__init__(**kwargs)
    #     # self.save()
    
    def exists(self, name, category, vendor, stock):
        """ if product exists, raise exception, if not, return False """
        existing_product = Product.objects(product_name=name, category=category, vendor=vendor, stock=stock).first()
        if existing_product:
            raise DuplicateProductError(message="This product exists")
        return False



def register_user(**kwargs):
    """ bundle registration of a User """
    user = User(**kwargs)
    try:
        user.save()
    except(DuplicateKeyError, NotUniqueError):
        profile = Vendor.objects(email=kwargs['email'])
        if profile:
            raise DuplicateVendorError("Already registered as a Vendor") from None
                # print("Duplicate product")
        # raise DuplicateUserError("This user has already been registered") from None
        print("User exists")
    else:
        print("Saved")
    return user

def register_vendor(**kwargs):
    """ handle converting of a User to a Vendor """
    user_profile = User.objects(_cls="User", email=kwargs['email']).first()
    if user_profile:
        try:
            user_details = json.loads(user_profile.to_json())
            # don't reset created at, save the same created date
            created_at = datetime.datetime.utcfromtimestamp(
                            user_details.pop('created_at')['$date']/1000)
            # print(type(created_at), created_at)
            vendor = Vendor(**user_details)
            vendor.created_at = created_at
            # updated _clas attribute
            vendor._cls = 'User.Vendor'
            vendor.role = 'vendor'
            # remove email from the newly passed in data
            kwargs.pop('email')
            # add the additional vendor details
            vendor_info = VendorInfo(**kwargs)
            vendor.vendor_details = vendor_info
            # save the vendor and delete user profile
            user_profile.delete()
            vendor.save()
        except Exception:
            raise
        return vendor
    else:
        raise UserNotFoundError("User not found")

# function to create and save product
def register_product(**kwargs):
    """ bundle creation and saving of product """
    product = Product(**kwargs)
    is_existing = False

    try:
        is_existing = product.exists(product.product_name, product.category, product.vendor, product.stock)
    except DuplicateProductError as e:
        print("Product error:", e)
    else:
        product.save()
    return product


try:
    user1 = register_user(
        **{
        "phone": "018-810",
        "email": "wisdom@mailer.com",
        "firstname": "Wisdom",
        "lastname": "Greens",
        "username": "GreenFarms",
        "password": "abc"
        }
    )

    user2 = register_user(
        **{
            "phone": "182-233",
            "email": "georgeamara@ymail.com",
            "firstname": "Amara",
            "lastname": "Goerge",
            "username": "amaregeorge",
            "password": "abc"
        }
    )

except (DuplicateKeyError, NotUniqueError):
    print("User exists")

try:
    user3 = register_user(
            **{
                "phone": "184-613",
                "email": "dullymutt@email.com",
                "firstname": "Dolly",
                "lastname": "Mutton",
                "username": "durlin",
                "password": "abc"
            }
        )
except DuplicateVendorError:
    print("Profile exists as a Vendor")

try:
    vendor1 = register_vendor(
        **{
            "email": "dullymutt@email.com",
            "farmname": "Dolly Meats",
            "location": "Zuba"
        }
    )
except UserNotFoundError as e:
    print(e)

# print([user.to_json() for user in User.objects(_cls='User')])
# print([vendor.to_json() for vendor in Vendor.objects()])
# print(Vendor.objects(email="dullymutt@email.com").first())
product1 = register_product(
    **{
        "product_name": "Cocoa",
        "category": "Roots/Tubers",
        "unit": "unit",
        "vendor": Vendor.objects(email="dullymutt@email.com").first(),
        "num_ratings": 0,
        "image_url": ["frontend/assets/images/product-images/default-product-image.jpg"],
        "price": 1695,
        "stock": 253,
        "rating": 5.0
    }
)

product2 = register_product(
    **{
        "product_name": "Beetroot",
        "category": "Roots/Tubers",
        "unit": "unit",
        "vendor": Vendor.objects(email="dullymutt@email.com").first(),
        "num_ratings": 0,
        "image_url": ["frontend/assets/images/product-images/default-product-image.jpg"],
        "price": 1614,
        "stock": 748,
        "rating": 4.0
    }
)

# print(product1.vendor)

engine.close_connection()
