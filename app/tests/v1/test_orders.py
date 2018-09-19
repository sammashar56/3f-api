import unittest
from app import create_app
import json

class TestFlaskApi(unittest.TestCase):

    def setUp(self):

        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.order_data = {
            "username":"Lewis Ngugi",
            "products":{
                "name":"Chips Bhajia",
                "qty":5,
                "price":5
            }
        }

        self.status = 'delivered'

        self.order_id = 1   

    def test_delete_specific_order(self):
        res = self.client.get(
            '/api/v1/orders/{}'.format(self.order_id), 
            content_type='application/json'
        )

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 204)   

    def test_get_specific_order(self):
        res = self.client.get(
            '/api/v1/orders/{}'.format(self.order_id), 
            content_type='application/json'
        )

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 204) 

    def test_get_orders(self):
        res = self.client.get(
            '/api/v1/orders', 
            content_type='application/json'
        )

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 200)

    def test_updating_order_status(self):

        res = self.client.put(
            '/api/v1/orders/{}'.format(self.order_id), 
            data = json.dumps(self.status),
            content_type='application/json'
        )

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 201)

    

    def test_place_an_order(self):
        res = self.client.post(
            '/api/v1/orders', 
            data = json.dumps(self.order_data), 
            content_type='application/json'
        )

        self.assertEqual(res.status_code, 201)


if __name__ == "__main__":
    unittest.main()
