from app.consumers.kafka_consumer import KafkaMessageConsumer

if __name__ == "__main__":
    consumer = KafkaMessageConsumer("student_created")
    consumer.start()