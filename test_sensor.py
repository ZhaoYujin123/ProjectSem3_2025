import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 17
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    print("Sensor test started. Press Ctrl+C to stop.")
    while True:
        moisture_value = GPIO.input(SENSOR_PIN)  
        if moisture_value == 0:
            status = "High Humidity (Soil is Wet)"
        else:
            status = "Low Humidity (Soil is Dry)"
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{current_time}] Sensor Value: {moisture_value} | {status}")
        time.sleep(2)  
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nSensor test stopped. GPIO cleaned up.")
