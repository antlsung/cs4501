from django.test import TestCase
import rest_framework, json, requests
from rest_framework.test import APIClient

class TestWeb(TestCase):
    def test_add_shoe(self):
        #create shoe
        response = requests.post('http://exp-api:8000/create_shoe/', data={'shoe':'ultraboost','brand':'adidas','text':'boost is life'})
        post_shoe = response.json()
        response_code = response.status_code
        id_shoe = str(post_shoe['id'])
        #check database
        check = requests.get('http://exp-api:8000/item_detail/?id='+id_shoe)
        get_shoe = check.json()

        self.assertEqual(response_code, 200)
        self.assertEqual(post_shoe, get_shoe)
        #remove test shoe from database
        delete = requests.post('http://exp-api:8000/delete_shoe/',data={'id':id_shoe})

    def test_add_user(self):
        #create user
        response = requests.post('http://exp-api:8000/create_user/', data={'name':'Nelson Mandela','address':'112 JPA','cart':'adilette slides'})
        post_user = response.json()
        response_code = response.status_code
        id_user = str(post_user['id'])
        #check database
        check = requests.get('http://exp-api:8000/user_detail/?id='+id_user)
        get_user = check.json()
        self.assertEqual(response_code, 200)
        self.assertEqual(post_user, get_user)
        #remove test user from database
        delete = requests.post('http://exp-api:8000/delete_user/',data={'id':id_user})

    # def setUp(self):
    #     shoes.objects.create(shoe='flyknit racer', brand='nike', text='first shoe for testing')
    #     users.objects.create(name='Ben Lee', address='1910 JPA', cart='shoe1, shoe2, shoe3')
    #     response = self.client.post('/shoes/')
    #     self.client = APIClient()
    #
    # def test_shoe_list_get(self):
    #     response = self.client.get('/shoes/')
    #     response_code = response.status_code
    #     self.assertEqual(response_code, 200)
    #
    # def test_shoe_list_post(self):
    #     response = self.client.post('/shoes/')
    #     response_code = response.status_code
    #     self.assertEqual(response_code, 400)
    #
    # def test_get_shoes_get(self):
    #     response = self.client.get('/get_shoes/',{'id': 1 })
    #     response_code = response.status_code
    #     data = json.loads(response.content.decode("utf-8"))
    #     self.assertEqual(response_code, 200)
    #     self.assertEqual(data['shoe'], "flyknit racer")
    #     self.assertEqual(data['brand'], "nike")
    #     self.assertNotEqual(data['text'], "")
    #
    # # This should fail
    # def test_get_shoes_post(self):
    #     response = self.client.post('/get_shoes/', {'id': 1})
    #     response_code = response.status_code
    #     data = json.loads(response.content.decode("utf-8"))
    #     self.assertEqual(response_code, 400)
    #
    # def test_methodtoaddshoes(self):
    #     response = self.client.post('/add_shoes/', {'shoe': 'clutchfit drive', 'brand': 'under armour', 'text': 'unit testing'}, format="json")
    #     response_code = response.status_code
    #     data = json.loads(response.content.decode("utf-8"))
    #     self.assertEqual(response_code, 201)
    #
    # def tearDown(self):
    #     pass
