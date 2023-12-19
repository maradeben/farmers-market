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
Date: Tue, 19 Dec 2023 15:18:13 GMT
Content-Type: application/json
Content-Length: 81
Access-Control-Allow-Origin: *
Connection: close

[
  "Grains",
  "Roots/Tubers",
  "Fruits/Vegetables",
  "Meat/Fish",
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
Date: Tue, 19 Dec 2023 15:18:40 GMT
Content-Type: application/json
Content-Length: 1055
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "6581a96d25daaa7b08d926a3"
    },
    "category": "Roots/Tubers",
    "created_at": {
      "$date": 1702999923829
    },
    "image_url": [
      "frontend/assets/images/product-images/roots-placeholder-image.png"
    ],
    "num_ratings": 0,
    "price": 1695.0,
    "product_name": "Cocoa",
    "rating": 5.0,
    "stock": 253,
    "unit": "unit",
    "vendor": {
      "$oid": "6581a96d25daaa7b08d926a0"
    },
    "vendor_email": "georgeamara@ymail.com",
    "vendor_location": "Suleja"
  },
  {
    "_id": {
      "$oid": "6581a96d25daaa7b08d926a8"
    },
    "category": "Oils",
    "created_at": {
      "$date": 1702999923829
    },
    "image_url": [
      "frontend/assets/images/product-images/oil-placeholder-image.png"
    ],
    "num_ratings": 0,
    "price": 6333.0,
    "product_name": "Peanut oil",
    "rating": 5.0,
    "stock": 841,
    "unit": "litre",
    "vendor": {
      "$oid": "6581a96d25daaa7b08d92698"
    },
    "vendor_email": "amosgoodwill@ymail.com",
    "vendor_location": "Abuja"
  }
]
```


**Retrieve Products**

GET /api/v1/products?limit=x

* Params:
  * limit(int)=999 - Optional.
      * Return the top selling products, limiting to the passed value, else returns top 999


```
curl -i http://127.0.0.1:5000/api/v1/products?limit=2
```


**Response**
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Tue, 19 Dec 2023 15:21:42 GMT
Content-Type: application/json
Content-Length: 1051
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "6581a96d25daaa7b08d926a2"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702999923829
    },
    "image_url": [
      "frontend/assets/images/product-images/grains-placeholder-image.png"
    ],
    "num_ratings": 0,
    "price": 999.0,
    "product_name": "Rice",
    "rating": 3.0,
    "stock": 619,
    "unit": "unit",
    "vendor": {
      "$oid": "6581a96d25daaa7b08d9269e"
    },
    "vendor_email": "ahmad.h@coldmail.com",
    "vendor_location": "Otukpo"
  },
  {
    "_id": {
      "$oid": "6581a96d25daaa7b08d926a3"
    },
    "category": "Roots/Tubers",
    "created_at": {
      "$date": 1702999923829
    },
    "image_url": [
      "frontend/assets/images/product-images/roots-placeholder-image.png"
    ],
    "num_ratings": 0,
    "price": 1695.0,
    "product_name": "Cocoa",
    "rating": 5.0,
    "stock": 253,
    "unit": "unit",
    "vendor": {
      "$oid": "6581a96d25daaa7b08d926a0"
    },
    "vendor_email": "georgeamara@ymail.com",
    "vendor_location": "Suleja"
  }
]
```

**Retrieve Products by category**

GET /api/v1/products/\<category\>?limit=x

* Params:
  * limit(int)=999 - Optional.
      * Return the top selling products, limiting to the passed value, else returns top 999

Where category is the product's category so:

*category_routes = {*  
    *'fruits-veggies': 'Fruits/Vegetables',*  
    *'grains': 'Grains',*  
    *'oils': 'Oils',*  
    *'meat-fish': 'Meat/Fish',*  
    *'roots-tubers': 'Roots/Tubers'*  
  *}*
```
curl -i http://127.0.0.1:5000/api/v1/products/grains?limit=2
```
**Response**
```
[
  {
    "_id": {
      "$oid": "6581a96d25daaa7b08d926a2"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702999923829
    },
    "image_url": [
      "frontend/assets/images/product-images/grains-placeholder-image.png"
    ],
    "num_ratings": 0,
    "price": 999.0,
    "product_name": "Rice",
    "rating": 3.0,
    "stock": 619,
    "unit": "unit",
    "vendor": {
      "$oid": "6581a96d25daaa7b08d9269e"
    },
    "vendor_email": "ahmad.h@coldmail.com",
    "vendor_location": "Otukpo"
  },
  {
    "_id": {
      "$oid": "6581a96d25daaa7b08d926aa"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702999923829
    },
    "image_url": [
      "frontend/assets/images/product-images/grains-placeholder-image.png"
    ],
    "num_ratings": 0,
    "price": 999.0,
    "product_name": "Corn",
    "rating": 4.0,
    "stock": 864,
    "unit": "unit",
    "vendor": {
      "$oid": "6581a96d25daaa7b08d926a1"
    },
    "vendor_email": "wisdom@mailer.com",
    "vendor_location": "Gombe"
  }
]
  ```


**Retrieve Single Product**

GET /api/v1/products/product/product_id

Retrieve product by product id

```
curl -i http://127.0.0.1:5000/api/v1/products/product/6581a96d25daaa7b08d926aa
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
    }HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Tue, 19 Dec 2023 15:24:54 GMT
Content-Type: application/json
Content-Length: 519
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "6581a96d25daaa7b08d926aa"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702999923829
    },
    "image_url": [
      "frontend/assets/images/product-images/grains-placeholder-image.png"
    ],
    "num_ratings": 0,
    "price": 999.0,
    "product_name": "Corn",
    "rating": 4.0,
    "stock": 864,
    "unit": "unit",
    "vendor": {
      "$oid": "6581a96d25daaa7b08d926a1"
    },
    "vendor_email": "wisdom@mailer.com",
    "vendor_location": "Gombe"
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
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Tue, 19 Dec 2023 15:25:23 GMT
Content-Type: application/json
Content-Length: 829
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_cls": "User.Vendor",
    "_id": {
      "$oid": "6581a96d25daaa7b08d92698"
    },
    "cart": [],
    "created_at": {
      "$date": 1702999923827
    },
    "email": "amosgoodwill@ymail.com",
    "firstname": "Amos",
    "lastname": "Goodwill",
    "role": "vendor",
    "vendor_details": {
      "farmname": "Amos Farm",
      "location": "Abuja",
      "num_ratings": 0,
      "rating": 0.0
    }
  },
  {
    "_cls": "User.Vendor",
    "_id": {
      "$oid": "6581a96d25daaa7b08d92699"
    },
    "cart": [],
    "created_at": {
      "$date": 1702999923827
    },
    "email": "bilua@starfarms.com",
    "firstname": "Ilua",
    "lastname": "Bilunde",
    "role": "vendor",
    "vendor_details": {
      "farmname": "Star Farms",
      "location": "Kogi",
      "num_ratings": 0,
      "rating": 0.0
    }
  }
]
```

**Retrieve Single Vendor**

GET /api/v1/vendor/vendor/vendor_id

Retrieve product by product id

```
curl -i http://127.0.0.1:5000/api/v1/vendors/vendor/6581a96d25daaa7b08d92699
```

**Response**

```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Tue, 19 Dec 2023 15:26:28 GMT
Content-Type: application/json
Content-Length: 519
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "_id": {
      "$oid": "6581a96d25daaa7b08d926aa"
    },
    "category": "Grains",
    "created_at": {
      "$date": 1702999923829
    },
    "image_url": [
      "frontend/assets/images/product-images/grains-placeholder-image.png"
    ],
    "num_ratings": 0,
    "price": 999.0,
    "product_name": "Corn",
    "rating": 4.0,
    "stock": 864,
    "unit": "unit",
    "vendor": {
      "$oid": "6581a96d25daaa7b08d926a1"
    },
    "vendor_email": "wisdom@mailer.com",
    "vendor_location": "Gombe"
  }
]
```