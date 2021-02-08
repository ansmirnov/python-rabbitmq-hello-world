import os

import pika

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST")
RABBITMQ_USER = os.environ.get("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD")

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)
)

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("Received %r" % body)

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
