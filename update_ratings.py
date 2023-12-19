from backend.models.vendor import Vendor

from backend.database.db_storage import storage_engine
import mongoengine
import random
random.seed(42)

mongoengine.disconnect('core')
storage_engine.close_connection()
storage_engine.connect()

vends = Vendor.objects()

for vend in vends:
    vend.vendor_details.rating = float(random.randint(3,5))
    vend.update(unset_rating=1)
    vend.save()
storage_engine.close_connection()