import pika
import sys
import random
import time
import datetime
from config import Config
import json

while True:
    try:
        connection = pika.BlockingConnection(
            pika.URLParameters(Config.BROKER_URL))
        break
    except Exception as error:
        print(f"Error {error}")
        time.sleep(4)

channel = connection.channel()

channel.queue_declare(queue='logs')
channel.queue_declare(queue='logsWebsocket')


channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.queue_bind('logs', exchange='logs')
channel.queue_bind('logsWebsocket', exchange='logs')


logs_type = ['INFO', 'WARNINGS', 'ERROR']
logs_type_probability = [0.47,0.47,0.05]
service_name = ['order', 'user', 'payment', 'invetory']

try:
    while True:
        time_sleep = random.randint(0, 2)
        type_choice = random.choices(logs_type, logs_type_probability)
        service=random.choice(service_name)
        current_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        if type_choice == 'ERROR':
            start_time = datetime.datetime()
            stop_time = start_time = datetime.timedelta(minutes=1)
            while datetime.datetime() < stop_time:
                log_message = {
                    "type": "ERROR",
                    "message": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus enim odio, dictum ac turpis in, elementum varius metus.",
                    "datetime": current_time,
                    "service": service
                }
                channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(log_message, indent=4))
            continue
        
        log_message = {
            "type": type_choice[0],
            "message": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus enim odio, dictum ac turpis in, elementum varius metus.",
            "datetime": current_time,
            "service": service
        }

        channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(log_message, indent=4))
        print(f" [x] Sent {log_message}")
except Exception as error:
    print(f'Error: {error}')
finally:
    connection.close()