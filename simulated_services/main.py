import pika
from config import Config
import time

connection = pika.BlockingConnection(
    pika.URLParameters(Config.BROKER_URL))


channel = connection.channel()

channel.queue_declare(queue='teste12343')
channel.queue_bind('teste12343', exchange='logs')

count = 0
while True:
    if count == 30:
        break
    time.sleep(1)
    count += 1

channel.queue_unbind('teste12343', exchange='logs')
channel.queue_delete('teste12343')
connection.close()