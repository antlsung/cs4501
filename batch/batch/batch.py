from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(['es'])

while True:
	try:
		consumer = KafkaConsumer('shoe-listings', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
		for message in consumer:
			# print(json.loads((message.value).decode('utf-8')))
			item_details = json.loads((message.value).decode('utf-8'))
			es.index(index='listing_index', doc_type='listing', id=item_details['id'], body=item_details)
			es.indices.refresh(index="listing_index")
		break
	except:
		pass
