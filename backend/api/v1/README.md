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

GET /api/v1/products/top-selling
```
curl -i http://127.0.0.1:5000/api/v1/products/top-selling
```
**Response**
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Sat, 16 Dec 2023 12:37:29 GMT
Content-Type: application/json
Content-Length: 4873
Access-Control-Allow-Origin: *
Connection: close

{
  "1c7392a8-65bc-4c75-984b-aa2e5f7a5a8d": {
    "category": "Fruits/Vegetables",
    "created_at": "2023-12-16T12:05:15.760704",
    "id": "1c7392a8-65bc-4c75-984b-aa2e5f7a5a8d",
    "image_url": "frontend/assets/images/product-images/default-product-image.jpg",
    "location": "Abuja",
    "name": "Tomato",
    "num_ratings": 0,
    "object": "Product",
    "price": 1939,
    "rating": 3.0,
    "stock": 843,
    "unit": "unit",
    "vendor_id": "d2366f15-ce6a-4e49-a694-3a58cbf1ec01"
  },
  ...
  "865eece2-fdae-489e-ba7d-c101d8b8ad3e": {
    "category": "Grains",
    "created_at": "2023-12-16T12:05:15.763076",
    "id": "865eece2-fdae-489e-ba7d-c101d8b8ad3e",
    "image_url": "frontend/assets/images/product-images/default-product-image.jpg",
    "location": "Gombe",
    "name": "Corn",
    "num_ratings": 0,
    "object": "Product",
    "price": 4545,
    "rating": 4.0,
    "stock": 864,
    "unit": "kg",
    "vendor_id": "eebdc76c-6723-4bc3-82b2-f524ec8dd848"
  }
}
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
Date: Sat, 16 Dec 2023 12:37:29 GMT
Content-Type: application/json
Content-Length: 4873
Access-Control-Allow-Origin: *
Connection: close

{
  "1c7392a8-65bc-4c75-984b-aa2e5f7a5a8d": {
    "category": "Fruits/Vegetables",
    "created_at": "2023-12-16T12:05:15.760704",
    "id": "1c7392a8-65bc-4c75-984b-aa2e5f7a5a8d",
    "image_url": "frontend/assets/images/product-images/default-product-image.jpg",
    "location": "Abuja",
    "name": "Tomato",
    "num_ratings": 0,
    "object": "Product",
    "price": 1939,
    "rating": 3.0,
    "stock": 843,
    "unit": "unit",
    "vendor_id": "d2366f15-ce6a-4e49-a694-3a58cbf1ec01"
  },
  "1ceb078f-983b-4524-9f38-a59ff1022320": {
    "category": "Meat/Poultry",
    "created_at": "2023-12-16T12:05:15.761206",
    "id": "1ceb078f-983b-4524-9f38-a59ff1022320",
    "image_url": "frontend/assets/images/product-images/default-product-image.jpg"...
  }
}
 
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
Date: Sat, 16 Dec 2023 12:48:43 GMT
Content-Type: application/json
Content-Length: 51464
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "8426cc5d-dbee-4e1c-b514-fe445fb66129": {
      "category": "Grains",
      "created_at": "2023-12-16T12:05:15.762180",
      "id": "8426cc5d-dbee-4e1c-b514-fe445fb66129",
      "image_url": "frontend/assets/images/product-images/default-product-image.jpg",
      "location": "Abuja",
      "name": "Corn",
      "num_ratings": 0,
      "object": "Product",
      "price": 2356,
      "rating": 5.0,
      "stock": 841,
      "unit": "unit",
      "vendor_id": "d2366f15-ce6a-4e49-a694-3a58cbf1ec01"
    }
  },
  {
    "865eece2-fdae-489e-ba7d-c101d8b8ad3e": {
      "category": "Grains",
      "created_at": "2023-12-16T12:05:15.763076",
      "id": "865eece2-fdae-489e-ba7d-c101d8b8ad3e",
      "image_url": "frontend/assets/images/product-images/default-product-image.jpg",
      "location": "Gombe",
      "name": "Corn",
      "num_ratings": 0,
      "object": "Product",
      "price": 4545,
      "rating": 4.0,
      "stock": 864,
      "unit": "kg",
      "vendor_id": "eebdc76c-6723-4bc3-82b2-f524ec8dd848"
    }
  }...
  ```

**Retrieve single product**

GET /api/v1/products/product/\<product_id\>
```curl http://127.0.0.1:5000/api/v1/products/product/865eece2-fdae-489e-ba7d-c101d8b8ad3e
```
**Response**
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Sat, 16 Dec 2023 12:43:43 GMT
Content-Type: application/json
Content-Length: 51464
Access-Control-Allow-Origin: *
Connection: close

{
      "category": "Grains",
      "created_at": "2023-12-16T12:05:15.763076",
      "id": "865eece2-fdae-489e-ba7d-c101d8b8ad3e",
      "image_url": "frontend/assets/images/product-images/default-product-image.jpg",
      "location": "Gombe",
      "name": "Corn",
      "num_ratings": 0,
      "object": "Product",
      "price": 4545,
      "rating": 4.0,
      "stock": 864,
      "unit": "kg",
      "vendor_id": "eebdc76c-6723-4bc3-82b2-f524ec8dd848"
}
```
___


## Vendors

API Routes for Vendors

**Retrieve Top Vendors**

GET /api/v1/vendors/top-vendors
```
 curl -i http://127.0.0.1:5000/api/v1/vendors/top-vendors
```
**Response**
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Sat, 16 Dec 2023 12:46:01 GMT
Content-Type: application/json
Content-Length: 4298
Access-Control-Allow-Origin: *
Connection: close

{
  "0ae197ff-be2b-4270-b6a2-d72493f79d10": {
    "created_at": "2023-12-16T12:05:10.046280",
    "email": "johnbull@ymail.com",
    "farmname": "Johhny JC",
    "firstname": "Bukola",
    "id": "0ae197ff-be2b-4270-b6a2-d72493f79d10",
    "lastname": "Johnson",
    "location": "Ilorin",
    "num_ratings": 0,
    "object": "Vendor",
    "phone": "858-991",
    "pswd": "abc",
    "rating": 3.0,
    "username": "johns_b"
  },
  "27668390-8529-4658-8f58-b75cc3d0b152": {
    "created_at": "2023-12-16T12:05:10.046677",
    "email": "ephman@cabmail.com",
    "farmname": "Ephraim&Manasseh",
    "firstname": "Ephraim",
    "id": "27668390-8529-4658-8f58-b75cc3d0b152",
    "lastname": "Manasseh",
    "location": "Nsukka",
    "num_ratings": 0,
    "object": "Vendor",
    "phone": "999-124",
    "pswd": "abc",
    "rating": 4.0,
    "username": "theman"
  }
}...
```
**Get single vendor**


GET api/v1/vendors/vendor/\<vendor_id\>
```curl http://127.0.0.1:5000/api/v1/vendors/vendor/0ae197ff-be2b-4270-b6a2-d72493f79d10
```
**Response**
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Sat, 16 Dec 2023 12:48:43 GMT
Content-Type: application/json
Content-Length: 51464
Access-Control-Allow-Origin: *
Connection: close

{
    "created_at": "2023-12-16T12:05:10.046280",
    "email": "johnbull@ymail.com",
    "farmname": "Johhny JC",
    "firstname": "Bukola",
    "id": "0ae197ff-be2b-4270-b6a2-d72493f79d10",
    "lastname": "Johnson",
    "location": "Ilorin",
    "num_ratings": 0,
    "object": "Vendor",
    "phone": "858-991",
    "pswd": "abc",
    "rating": 3.0,
    "username": "johns_b"
  }
```
