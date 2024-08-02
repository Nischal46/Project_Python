from kafka import KafkaConsumer
import json

current_orders = {}

def process_order(order):
    # Implement the logic to process the order data
    print("Received order:", order)
    # For example, you can save the order data to a database or perform other actions

consumer = KafkaConsumer(
    'order_notifications',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='order_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    key_deserializer=lambda x: x.decode('utf-8')
)

for message in consumer:
    order_data = message.value
    order_id = message.key
    print(f'Processing order with ID: {order_id}')
    process_order(order_data)
