from django.test import TestCase
from jbay.models import shoes, users
import rest_framework, json
from rest_framework.test import APIClient

class TestShoeApi(TestCase):
    def setUp(self):
        shoes.objects.create(shoe='flyknit racer', brand='nike', text='first shoe for testing')
        users.objects.create(name='Ben Lee', address='1910 JPA', cart='shoe1, shoe2, shoe3')
        self.client = APIClient()

    def test_shoe_list_get(self):
        response = self.client.get('/shoes/')
        response_code = response.status_code
        self.assertEqual(response_code, 200)

    def test_shoe_list_post(self):
        response = self.client.post('/shoes/')
        response_code = response.status_code
        self.assertEqual(response_code, 400)

    def test_get_shoes_get(self):
        response = self.client.get('/get_shoes/',{'id': 1 })
        response_code = response.status_code
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response_code, 200)
        self.assertEqual(data['shoe'], "flyknit racer")
        self.assertEqual(data['brand'], "nike")
        self.assertNotEqual(data['text'], "")

    # This should fail
    def test_get_shoes_post(self):
        response = self.client.post('/get_shoes/', {'id': 1})
        response_code = response.status_code
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response_code, 400)

    def test_methodtoaddshoes(self):
        response = self.client.post('/add_shoes/', {'shoe': 'clutchfit drive', 'brand': 'under armour', 'text': 'unit testing'}, format="json")
        response_code = response.status_code
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response_code, 201)





    def tearDown(self):
        pass
