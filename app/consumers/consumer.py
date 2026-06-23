from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "student_created",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda x: json.loads(x.decode())
)

for msg in consumer:

    try:

        student = msg.value

        print(student)

        # simulate processing

        if student["name"] == "error":
            raise Exception("Processing failed")

    except Exception:

        producer.send("student_dlq", student)