# Fast Food Fast   [![Maintainability](https://api.codeclimate.com/v1/badges/a45a0bad4d14790897c1/maintainability)](https://codeclimate.com/github/tesh254/3f-api/maintainability) [![Coverage Status](https://coveralls.io/repos/github/tesh254/3f-api/badge.svg?branch=develop)](https://coveralls.io/github/tesh254/3f-api?branch=develop)          [![Build Status](https://travis-ci.org/tesh254/3f-api.svg?branch=develop)](https://travis-ci.org/tesh254/3f-api)


This is the repository holds the api endpoints for [Fast Food Fast](https://github.com/3f.git). 

To tests and play with the api you need to follow a number of steps for the api to work fully

First you'll need to clone the repository or you can visit my hosted heroku site here [https://fastfoodfast254.herokuapp.com](https://fastfoodfast254.herokuapp.com).

Install the requirements or third party library dependencies using the below command

```bash
$pip install -r requirements.txt
```

To run the app and test the apis on postman or any similar software like curl type this command

```bash
$python run.py
```

You can choose to test the api's on postman using the remote url of the api hosted on heroku.

Open postman, and try this endpoints

|Endpoint|Function|
|--------|--------|
| `GET /api/v1/orders`|This endpoint gets all orders. 
| `GET /api/v1/orders/<id>`|This api gets a specific order.
| `POST /api/v1/orders`|This api creates a new order.
| `PUT /api/v1/orders/<id>`|This api updates an order status.
| `DELETE /api/v1/orders/<id>`|This api deletes an order.


## GET all orders

When this is api is requested it returns all orders in json format as shown below:

```json
{
    "orders": [
        {
            "id": 1,
            "username": "Lenson Gita",
            "products": {
                "name": "Pizza",
                "qty": 1,
                "price": 1000
            },
            "status": "Pending",
            "ordered_date": "2018-09-20 00:03:20.994632",
            "delivered_date": null
        },
        {
            "id": 2,
            "username": "Jeremy Fisher",
            "products": {
                "name": "French Fries",
                "qty": 1,
                "price": 1000
            },
            "status": "Pending",
            "ordered_date": "2018-09-20 00:03:21.873132",
            "delivered_date": null
        }
    ]
}
```

If there are no orders yet then a json similar to this will be shown:

```json
{
    "message": "No orders yet"
}
```

Meaning an order must be placed for it to appear here.

## POST place order

To use this api endpoint you need to send a json format file to get a response as shown:

```json
{
    "username":"Mikana Jusi",
    "products":{
        "name":"Hamburger",
        "qty":1,
        "price":500
    }
}
```

As you may have noticed the fields in this request json lacks fields to call it an order, the reason is the server only needs to be sent this specified fields in order the rest of the fields are autogenerated i.e. status is pending, ordered_date is the tim e of placing an order, id is autoincrement according to your orders length.

## GET specific order by id

By requesting an order of the id specified at the url, if there is an order the status returned will be `200 OK` for a success with the order object but if there is no order of that id then a `404 Not Found` error status will be sent 

## PUT specific order by id

By using this endpoint an responding with a json object of the order status 