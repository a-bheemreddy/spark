from kafka import KafkaProducer
import json
import time

BOOTSTRAP_SERVER = 'localhost:9099'

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers=[BOOTSTRAP_SERVER],
    value_serializer=json_serializer
)

def Create_Kafka_Topic(topic_name):
    from kafka.admin import KafkaAdminClient, NewTopic
    admin_client = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVER)
    topic_list = []
    topic_list.append(NewTopic(name=topic_name, num_partitions=1, replication_factor=1))
    existing_topics = admin_client.list_topics()
    if topic_name not in existing_topics:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
    else:
        print(f"Topic '{topic_name}' already exists.")
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

if __name__ == "__main__":
    #Create_Kafka_Topic("test")
    for i in range(10):
        sample_data = {"number": i}
        producer.send("sample_topic", sample_data)
        print(f"Sent: {sample_data}")
        time.sleep(1)

    producer.flush()
    producer.close()