#!/usr/bin/env python3.9
""" testing file """
from backend.models.base import BaseModel
from backend.models.product import Product
from backend.models.vendor import Vendor
from backend.database import file_store
from PIL import Image

image_path = 'frontend/assets/images/product-images/default-product-image.jpg'
image = Image.open(image_path)
image.show()
# new = BaseModel()
# print(new.to_dict())
# prod = Product()
# print(prod)
prod1 = Product("Isu ewura", "Roots/Tubers", 1000, 'unit', 200, 'vid')
# print(prod1.to_dict())
# prod2 = Product("Isu ewura", "Roots/Tuber", '1000', 200, 'vid')
# print(prod2.to_dict())
props = {
    "name": "Bag of rice",
    "category": "Grains",
    "price": 15000,
    "unit": 'Bag',
    "stock": 30,
    "vendor_id": 'alupupu'
}
prod3 = Product(**props)
# print(prod3.to_dict())
# print(products_list)
file_store.save()

prod1.incr_stock(23)
prod3.update_rating(5)
prod3.decr_stock(8)
prod3.price = 18000
# print(prod1.to_dict())
# print(prod3.to_dict())

# print(products_list)


vendor1 = Vendor('1234', 'vend1@mail.com', 'Adiba', 'Rokos', 'adiroks', 'Adiba Greens', 'Oketu')
# print(vendor1)

props2 = {
    'phone': '333-444',
    'email': 'olubimu@ymail.com',
    'firstname': 'Ignition',
    'lastname': 'Engine',
    'username': 'enging',
    'farmname': 'Engineering Farm',
    'location': 'Kuja'
}

vendor2 = Vendor(**props2)

file_store.save()
print("Here's the saved file")
print(file_store.all())

# file_store.clear_storage()
# print("\n\nAfter clear")
# print(file_store.all())
