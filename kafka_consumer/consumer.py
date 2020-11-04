from kafka import KafkaConsumer, KafkaProducer
from pymongo import MongoClient
from bson.json_util import loads

if __name__ == '__main__':

    # database
    client = MongoClient('mongodb://localhost:27017')
    db = client['twitter']
    collection = db['tweets']

    # kafka
    topic_name = 'json-topic'
    consumer = KafkaConsumer(topic_name, 
        auto_offset_reset='earliest', 
        bootstrap_servers=['localhost:9092'], 
        api_version=(0, 10), 
        consumer_timeout_ms=10000)

    # kafka to mongo
    for msg in consumer:
        collection.insert_one(loads(msg.value))

    # close kafka connection
    consumer.close()
