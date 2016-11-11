from django.test import TestCase
import json, requests, re
from kafka import KafkaProducer, KafkaConsumer
from elasticsearch import Elasticsearch

class TestExp(TestCase):

    def test_send_shoe_kafka(self):
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        shoe_new_listing = {'id':11,'shoe':'ultraboost','brand':'adidas','text':'boost is life','published_date':'2016-11-10T20:47:47.972330Z'}
        response = producer.send('shoe-listings', json.dumps(shoe_new_listing).encode('utf-8'))
        consumer = KafkaConsumer('shoe-listings', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])

        #Checking sent status through making sure .send() response follows the format "<kafka.producer.future.FutureRecordMetadata"
        #string .find() returns index of 0 if "<kafka.producer..." is found.
        #Bool() of 0 is false, so we assertFalse to check if the producer successfully sent
        self.assertFalse(bool(str(response).find("<kafka.producer.future.FutureRecordMetadata")))


    def test_elasticsearch(self):
        es = Elasticsearch(['es'])
        item_details = {'id':12,'shoe':'air monarch','brand':'nike','text':'air is life','published_date':'2016-11-10T20:47:47.972330Z'}
        es.index(index='listing_index', doc_type='listing', id=item_details['id'], body=item_details)
        results = es.search(index='listing_index', body={'query': {'query_string': {'query':"monarch"}}, 'size': 10})
        shoe_results = results['hits']['hits']
        search_shoes = []
        for shoe in shoe_results:
            search_shoes.append(shoe['_source'])
        # print(search_shoes[0]['shoe'])
        self.assertEqual(search_shoes[0]['shoe'],"air monarch")


    def tearDown(self):
        pass
