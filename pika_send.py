#!/usr/bin/env python
import pika

# Setup the Credentials for the connection.
credentials = pika.PlainCredentials('weather', 'IrvogAyn')

# Setup the ConnectionParameters for the connection.
connectionParams = pika.ConnectionParameters(host='54.214.1.82',
                                            port=5672,
                                            #virtual_host='/weather',
                                            credentials=credentials)

connection = pika.BlockingConnection(connectionParams)
channel = connection.channel()

'''
channel.queue_declare(queue='weather_trace')

channel.queue_bind(exchange='amq.rabbitmq.trace',
                   queue='weather_trace',
                   routing_key='deliver.weather_trace')


channel.basic_publish(exchange='amq.rabbitmq.trace',
                      routing_key='hello',
                      body='Hello World!')
'''

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print " [x] Sent 'Hello World!'"

connection.close()