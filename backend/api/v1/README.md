# API V1

* [Products](#products)
* [Vendors](#vendors)


## Products
API Routes for Products:


**Get product categories**

GET /api/v1/products/categories
```
curl -i http://127.0.0.1:5000/api/v1/products/categories
```
**Response**
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Sat, 16 Dec 2023 12:36:22 GMT
Content-Type: application/json
Content-Length: 84
Access-Control-Allow-Origin: *
Connection: close

[
  "Grains",
  "Roots/Tubers",
  "Fruits/Vegetables",
  "Meat/Poultry",
  "Oils"
]
```


**Top selling products**

GET /api/v1/products/top-selling?limit=x

* Params:
  * limit(int)=20 - Optional.
      * Return the top selling products, limiting to the passed value, else returns top 20

```
curl -i http://127.0.0.1:5000/api/v1/products/top-selling?limit=2
```
**Response**
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Mon, 18 Dec 2023 01:35:38 GMT
Content-Type: application/json
Content-Length: 925
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "657f44f977e9bc4c33428ee7"
    },
    "category": "Roots/Tubers",
    "created_at": {
      "$date": 1702866539265
    },
    "image_url": [
      "frontend/assets/images/product-images/default-product-image.jpg"
    ],
    "location": "Gombe",
    "name": "Cocoa",
    "num_ratings": 0,
    "price": 1695.0,
    "rating": 5.0,
    "stock": 253,
    "unit": "unit",
    "vendor": {
      "$oid": "657f413c77e9bc4c33428ee6"
    }
  },
  {
    "_id": {
      "$oid": "657f44fa77e9bc4c33428eec"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702866539265
    },
    "image_url": [
      "frontend/assets/images/product-images/default-product-image.jpg"
    ],
    "location": "Kogi",
    "name": "Corn",
    "num_ratings": 0,
    "price": 2356.0,
    "rating": 5.0,
    "stock": 841,
    "unit": "unit",
    "vendor": {
      "$oid": "657f413977e9bc4c33428ede"
    }
  }
]
```


**Retrieve Products**

GET /api/v1/products
```
curl -i http://127.0.0.1:5000/api/v1/products/
```
**Response**
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Mon, 18 Dec 2023 01:39:42 GMT
Content-Type: application/json
Content-Length: 925
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "657f44fd77e9bc4c334290b3"
    },
    "category": "Fruits/Vegetables",
    "created_at": {
      "$date": 1702866539265
    },
    "image_url": [
      "frontend/assets/images/product-images/default-product-image.jpg"
    ],
    "location": "Kogi",
    "name": "Water leaf",
    "num_ratings": 0,
    "price": 814.0,
    "rating": 4.0,
    "stock": 789,
    "unit": "unit",
    "vendor": {
      "$oid": "657f413977e9bc4c33428ede"
    }
  },
  {
    "_id": {
      "$oid": "657f44fd77e9bc4c334290b4"
    },
    "category": "Meat/Poultry",
    "created_at": {
      "$date": 1702866539265
    },
    "image_url": [
      "frontend/assets/images/product-images/default-product-image.jpg"
    ],
    "location": "Ijebu",
    "name": "Goat",
    "num_ratings": 0,
    "price": 9448.0,
    "rating": 3.0,
    "stock": 559,
    "unit": "kg",
    "vendor": {
      "$oid": "657f413b77e9bc4c33428ee4"
    }
  }
  ...
]
 
```

**Retrieve Products by category**

GET /api/v1/products/\<category\>

Where category is the product's category so:

*category_routes = {*  
    *'fruits-veggies': 'Fruits/Vegetables',*  
    *'grains': 'Grains',*  
    *'oils': 'Oils',*  
    *'meat-poultry': 'Meat/Poultry',*  
    *'roots-tubers': 'Roots/Tubers'*  
  *}*
```
curl -i http://127.0.0.1:5000/api/v1/products/grains
```
**Response**
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Mon, 18 Dec 2023 01:43:51 GMT
Content-Type: application/json
Content-Length: 925
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "657f44fb77e9bc4c33428fd7"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702866539265
    },
    "image_url": [
      "frontend/assets/images/product-images/default-product-image.jpg"
    ],
    "location": "Kogi",
    "name": "Wheat",
    "num_ratings": 0,
    "price": 10908.0,
    "rating": 5.0,
    "stock": 983,
    "unit": "kg",
    "vendor": {
      "$oid": "657f413977e9bc4c33428ede"
    }
  },
  {
    "_id": {
      "$oid": "657f44fb77e9bc4c33428fd8"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702866539265
    },
    "image_url": [
      "frontend/assets/images/product-images/default-product-image.jpg"
    ],
    "location": "Kogi",
    "name": "Corn",
    "num_ratings": 0,
    "price": 10908.0,
    "rating": 3.0,
    "stock": 484,
    "unit": "kg",
    "vendor": {
      "$oid": "657f413977e9bc4c33428ede"
    }
  },
  {
    "_id": {
      "$oid": "657f44fc77e9bc4c33428fe2"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702866539265
    },
    "image_url": [
      "frontend/assets/images/product-images/default-product-image.jpg"
    ],
    "location": "Gombe",
    "name": "Rice",
    "num_ratings": 0,
    "price": 1195.0,
    "rating": 5.0,
    "stock": 615,
    "unit": "unit",
    "vendor": {
      "$oid": "657f413c77e9bc4c33428ee6"
    }
  }
  ...
]
  ```


**Retrieve Single Product**

GET /api/v1/products/product/product_id

Retrieve product by product id

```
curl -i http://127.0.0.1:5000/api/v1/products/product/657f44fc77e9bc4c33428fe2
```

**Response**

```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Mon, 18 Dec 2023 01:47:27 GMT
Content-Type: application/json
Content-Length: 461
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "657f44fc77e9bc4c33428fe2"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702866539265
    },
    "image_url": [
      "frontend/assets/images/product-images/default-product-image.jpg"
    ],
    "location": "Gombe",
    "name": "Rice",
    "num_ratings": 0,
    "price": 1195.0,
    "rating": 5.0,
    "stock": 615,
    "unit": "unit",
    "vendor": {
      "$oid": "657f413c77e9bc4c33428ee6"
    }
  }
]
```
___




## Vendors

API Routes for Vendors


**Retrieve Top Vendors**

Params:
  * limit(int)=20 - Optional.
      * Return the top selling products, limiting to the passed value, else returns top 20

GET /api/v1/vendors/top-vendors?limit=x
```

 curl -i http://127.0.0.1:5000/api/v1/vendors/top-vendors?limit=2
```
**Response**

```
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Mon, 18 Dec 2023 01:50:05 GMT
Content-Type: application/json
Content-Length: 735
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "657f407777e9bc4c33428eda"
    },
    "created_at": {
      "$date": 1702841383435
    },
    "email": "amosgoodwill@ymail.com",
    "farmname": "Amos Farm",
    "firstname": "Amos",
    "lastname": "Goodwill",
    "location": "Abuja",
    "num_ratings": 0,
    "phone": "123-456",
    "rating": 5.0,
    "username": "amogood"
  },
  {
    "_id": {
      "$oid": "657f413a77e9bc4c33428ee0"
    },
    "created_at": {
      "$date": 1702841383435
    },
    "email": "chiakpan@fresh.com",
    "farmname": "Chi Fresh Produce",
    "firstname": "Chinonso",
    "lastname": "Akpan",
    "location": "Ibadan",
    "num_ratings": 0,
    "phone": "111-111",
    "rating": 5.0,
    "username": "apk_chi"
  }
  ...
]
```

**Retrieve Single Vendor**

GET /api/v1/vendor/vendor/vendor_id

Retrieve product by product id

```
curl -i http://127.0.0.1:5000/api/v1/vendors/vendor/657f407777e9bc4c33428eda
```

**Response**

```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Mon, 18 Dec 2023 01:52:23 GMT
Content-Type: application/json
Content-Length: 366
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "657f407777e9bc4c33428eda"
    },
    "created_at": {
      "$date": 1702841383435
    },
    "email": "amosgoodwill@ymail.com",
    "farmname": "Amos Farm",
    "firstname": "Amos",
    "lastname": "Goodwill",
    "location": "Abuja",
    "num_ratings": 0,
    "phone": "123-456",
    "rating": 5.0,
    "username": "amogood"
  }
]
```