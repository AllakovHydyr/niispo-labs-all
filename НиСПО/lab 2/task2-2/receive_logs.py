import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Объявляем exchange типа fanout
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Создаем временную очередь (exclusive=True)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Привязываем очередь к exchange
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()