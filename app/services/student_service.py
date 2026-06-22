from app.producers.kafka_producer import KafkaMessageProducer

producer = KafkaMessageProducer()


class StudentService:

    def create_student(self, db, student_data):

        student_dict = {
            "name": student_data.name,
            "email": student_data.email,
            "age": student_data.age
        }

        # Send event to Kafka instead of direct DB write
        producer.send("student_created", student_dict)

        return student_dict