""" miscellaneous tests """
from backend.database.product_ops import *
from backend.database.vendor_ops import *
from backend.database.db_storage import storage_engine, DBStorage

# test connection
# collections = mongoengine.connection.get_db().list_collection_names()
# print(collections)

# products = get_products()
# print(products[1])
# top_prods = get_top_products(2)
# print(top_prods)
# print(get_products('grains'))
# print(get_single_product("657f44fd77e9bc4c334290bb"))
print(get_top_vendors(4))

# close connection
storage_engine.close_connection()
