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
'''

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      #queue='weather_trace',
                      queue='hello',
                      no_ack=True)

channel.start_consuming()