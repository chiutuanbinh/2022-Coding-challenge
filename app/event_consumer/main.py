

from flask import Flask

app = Flask('myapp')
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

def handler(ch, method, properties, body):
    print(body)
channel.queue_declare(queue='events')
# channel.basic_publish(exchange='', routing_key='events', body='Hello World!')
# channel.basic_publish(exchange='', routing_key='events', body='Hello World!')
# channel.basic_publish(exchange='', routing_key='events', body='Hello World!')
channel.basic_consume(queue='events',
                      auto_ack=True,
                      on_message_callback=handler)
channel.start_consuming()

def get_state():
    pass

@app.route('/api/v1/state', methods=['GET'])
def state():
    




    pass

app.run('0.0.0.0', '8000')