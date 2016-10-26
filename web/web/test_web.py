from django.test import TestCase
import rest_framework, json, requests
from rest_framework.test import APIClient

class TestWeb(TestCase):
#unit test won't work due to authenticator

    # def test_add_shoe(self):
    #     #create shoe
    #     response = requests.post('http://exp-api:8000/create_shoe/', data={'shoe':'ultraboost','brand':'adidas','text':'boost is life','auth':'pbkdf2_sha256$20000$0sNrukA5skBw$jgJVJuacH55D2RqxAl/Sz6EJDEKs93niIM9h4zZk9es='})
    #     print(response.content)
    #     post_shoe = response.json()
    #     response_code = response.status_code
    #     id_shoe = str(post_shoe['id'])
    #     #check database
    #     check = requests.get('http://exp-api:8000/item_detail/?id='+id_shoe)
    #     get_shoe = check.json()
    #
    #     self.assertEqual(response_code, 200)
    #     self.assertEqual(post_shoe, get_shoe)
    #     #remove test shoe from database
    #     delete = requests.post('http://exp-api:8000/delete_shoe/',data={'id':id_shoe})
#unit test won't work due to authenticator
    # def test_delete_shoe(self):
    #     #create shoe
    #     response = requests.post('http://exp-api:8000/create_shoe/', data={'shoe':'ultraboost','brand':'adidas','text':'boost is life'})
    #     post_shoe = response.json()
    #     id_shoe = str(post_shoe['id'])
    #     #delete shoe
    #     delete = requests.post('http://exp-api:8000/delete_shoe/',data={'id':id_shoe})
    #     delete_code = delete.status_code
    #
    #     #check database
    #     check = requests.get('http://exp-api:8000/item_detail/?id='+id_shoe)
    #     check_code = check.status_code
    #
    #     #test deletion status code and finding item in database status code (so 200 succesful delete and 400 for not finding item after delete)
    #     self.assertEqual(delete_code, 200)
    #     self.assertEqual(check_code, 400)
    def test_add_user(self):
        #create user
        response = requests.post('http://exp-api:8000/create_user/', data={'name':'Nelson Mandela','password': 'nelson1','address':'112 JPA','cart':'adilette slides'})
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



    def test_delete_user(self):
        #create shoe
        response = requests.post('http://exp-api:8000/create_user/', data={'name':'Harold Kumar','password': 'kumar1','address':'112 adfsad','cart':'adidas superstars'})
        post_user = response.json()
        id_user = str(post_user['id'])

        #delete shoe
        delete = requests.post('http://exp-api:8000/delete_user/',data={'id':id_user})
        delete_code = delete.status_code
        #check database
        check = requests.get('http://exp-api:8000/user_detail/?id='+id_user)
        check_code = check.status_code
        #test deletion status code and finding item in database status code (so 200 succesful delete and 400 for not finding item after delete)
        self.assertEqual(delete_code, 200)
        self.assertEqual(check_code, 400)

    def tearDown(self):
        pass
