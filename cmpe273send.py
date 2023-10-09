import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for x in range(10000):
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World! - ' + str(x))
    print("Message " + str(x) + " Sent")

connection.close()