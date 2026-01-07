import RPi.GPIO as GPIO
import time
import csv
from datetime import datetime

GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 17
GPIO.setup(SENSOR_PIN, GPIO.IN)

CSV_FILE = "sensor_data.csv"

try:
    with open(CSV_FILE, 'r') as f:
        pass
except FileNotFoundError:
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Moisture_Value', 'Humidity_Status'])
try:
    print("Data collection started. Press Ctrl+C to stop.")
    print(f"Data will be saved to {CSV_FILE} (every 30 minutes).")
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        moisture_val = GPIO.input(SENSOR_PIN)
        humidity_status = "Wet" if moisture_val == 0 else "Dry"
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, moisture_val, humidity_status])
        print(f"[{timestamp}] Data recorded: {moisture_val}, {humidity_status}")
        time.sleep(1800)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nData collection stopped. GPIO cleaned up.")
except Exception as e:
    GPIO.cleanup()
    print(f"\nError occurred: {e}")
    print("GPIO cleaned up.")
