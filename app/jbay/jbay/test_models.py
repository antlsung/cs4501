from django.test import TestCase
from jbay.models import shoes, users
import rest_framework

class ShoesTestCase(TestCase):
	def setUp(self):
		shoes.objects.create(shoe='flyknit racer', brand='nike',text='first shoe for testing')

	def test_shoes_are_created(self):
		racer = shoes.objects.get(shoe='flyknit racer')
		self.assertNotEqual(str(racer), "racer")
		self.assertNotEqual(str(racer),"FLYKNIT RACER")
		self.assertNotEqual(str(racer),"")
		self.assertEqual(str(racer), "flyknit racer")

	def tearDown(self):
		pass

class UsersTestCase(TestCase):
	def setUp(self):
		users.objects.create(name='Ben Lee', address='1910 JPA',cart='shoe1, shoe2, shoe3')

	def test_users_are_created(self):
		user = users.objects.get(name='Ben Lee')
		self.assertNotEqual(str(user), "ben lee")
		self.assertNotEqual(str(user), "other bad name")
		self.assertNotEqual(str(user), "")
		self.assertEqual(str(user), "Ben Lee")

	def tearDown(self):
		pass