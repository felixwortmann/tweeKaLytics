from kafka import KafkaConsumer, KafkaProducer

if __name__ == '__main__':
    print('Running Consumer..')
    parsed_records = []
    topic_name = 'raw_recipes'
    parsed_topic_name = 'parsed_recipes'

    consumer = KafkaConsumer(topic_name, 
        auto_offset_reset='earliest', 
        bootstrap_servers=['kafka-service-tweekalytics:9092'], 
        api_version=(0, 10), 
        consumer_timeout_ms=1000)
    for msg in consumer:
        value = msg.value
    consumer.close()