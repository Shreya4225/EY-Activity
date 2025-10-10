import pika
import json

# connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a queue (idempotent - creates only if not existing)
channel.queue_declare(queue="student_tasks")

# prepare a message
task= {
    "student_id": 101,
    "action": "generate_certificate",
    "email": "rahul@example.com"
}

# publish the message to the queue
channel.basic_publish(
    exchange='',
    routing_key='student_tasks',
    body=json.dumps(task)
)

print("task sent to queue", task)

connection.close()