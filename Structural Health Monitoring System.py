import time
import random

# Simulated thresholds for safe values
THRESHOLDS = {
    "strain": 50.0,       # microstrain
    "vibration": 0.5,     # g-force
    "temperature": 60.0   # degrees Celsius
}

def read_sensor_data():
    """Simulate reading sensor data"""
    return {
        "strain": random.uniform(20.0, 70.0),
        "vibration": random.uniform(0.1, 1.0),
        "temperature": random.uniform(25.0, 80.0)
    }

def analyze_data(data):
    """Analyze the sensor data and check for threshold violations"""
    alerts = []
    for key, value in data.items():
        if value > THRESHOLDS[key]:
            alerts.append(f"ALERT: {key.capitalize()} too high ({value:.2f})!")
    return alerts

def monitor_structure():
    """Main monitoring loop"""
    print("Starting Structural Health Monitoring...\n")
    for _ in range(5):  # Simulate 5 readings
        data = read_sensor_data()
        print(f"Sensor Data: {data}")
        alerts = analyze_data(data)
        for alert in alerts:
            print(alert)
        print("-" * 40)
        time.sleep(1)  # Simulate delay between readings

if __name__== "__main__":
    monitor_structure()
