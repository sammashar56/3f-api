from flask import Flask, request, abort
from flask_restful import Resource, Api
import datetime

app = Flask(__name__)

api = Api(app)

orders = []
class Orders(Resource):
    def get(self):
        
        if len(orders) == 0:
            return ({
                "message":"No orders yet"
            }),201
        return (
            {
                "orders":orders
            }            
        ), 201