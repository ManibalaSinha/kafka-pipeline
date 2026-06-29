from app.consumers.kafka_consumer import KafkaMessageConsumer

class RetryConsumer(KafkaMessageConsumer):
    def __init__(self):
        super().__init__()

        # override topic
        self.consumer.subscribe(["student_created_retry"])


if __name__ == "__main__":
    consumer = RetryConsumer()
    consumer.start()