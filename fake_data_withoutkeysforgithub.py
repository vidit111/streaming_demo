import time
import json
import random
from azure.eventhub import EventHubProducerClient, EventData

# Replace with your Event Hub connection details
EVENT_HUB_CONNECTION_STR = ""
EVENT_HUB_NAME = ""

# Function to generate sample data
def generate_weather_data():
    return {
        "temperature": random.randint(15, 40),
        "humidity": random.randint(10, 90),
        "windSpeed": random.randint(0, 30),
        "windDirection": random.choice(["N", "S", "E", "W", "NE", "NW", "SE", "SW"]),
        "precipitation": random.randint(0, 10),
        "conditions": random.choice(["sunny", "cloudy", "rainy", "stormy", "foggy"])
    }

# Initialize Event Hub Producer
producer = EventHubProducerClient.from_connection_string(
    conn_str=EVENT_HUB_CONNECTION_STR, 
    eventhub_name=EVENT_HUB_NAME
)

message_count = 0
# Send data in a loop
while True:
    event_data = json.dumps(generate_weather_data())  # Convert to JSON
    event_batch = producer.create_batch()
    event_batch.add(EventData(event_data))
    producer.send_batch(event_batch)
    message_count += 1
    print("Message no.\n",message_count)
    print(f"Sent: {event_data}")  # Log what was sent
    time.sleep(15)  # Send every 5 seconds
