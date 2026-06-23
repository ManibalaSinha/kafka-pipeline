from app.producers.kafka_producer import KafkaMessageProducer


class StudentService:
    def __init__(self):
        self.producer = KafkaMessageProducer()

    def create_student(self, db, student_data):
        student_dict = {
            "name": student_data.name,
            "email": student_data.email,
            "age": student_data.age,
        }

        # Send event to Kafka
        self.producer.send("student_created", student_dict)

        return student_dict