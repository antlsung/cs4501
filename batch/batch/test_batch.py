from django.test import TestCase
from elasticsearch import Elasticsearch

class IndexTestCase(TestCase):
	def setUp(self):
		pass

	def test_index_shoe(self):
		nike_test = {'shoe':'flyknit racer', 'brand':'nike', 'text':'first shoe for testing','id':1}
		# adidas_test = {'shoe':'ultra boost', 'brand':'adidas', 'text':'second shoe for testing','id':2}
		es = Elasticsearch(['es'])
		es.index(index='listing_index', doc_type='listing', id=nike_test['id'], body=nike_test)
		# es.index(index='listing_index', doc_type='listing', id=adidas_test['id'], body=adidas_test)
		es.indices.refresh(index="listing_index")
		result = es.search(index='listing_index', body={'query': {'query_string': {'query': 'nike'}}, 'size': 10})
		shoe = result['hits']['hits'][0]['_source']
		self.assertEqual(str(shoe['shoe']), nike_test['shoe'])
		self.assertEqual(str(shoe['brand']), nike_test['brand'])
		self.assertEqual(str(shoe['text']), nike_test['text'])

	def tearDown(self):
		pass