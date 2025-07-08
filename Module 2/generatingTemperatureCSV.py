import csv
from datetime import datetime, timedelta
import random


def generate_mock_temperature_csv(filename='temperatures.csv',
                                  start_time='2025-07-08 06:00:00',
                                  readings=100):
    start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'temperature'])

        current_time = start
        temp = 20.0  # starting temperature

        for _ in range(readings):
            # Simulate temperature fluctuations
            temp += random.uniform(-0.5, 0.5)
            writer.writerow([current_time.strftime('%Y-%m-%d %H:%M:%S'), round(temp, 2)])
            current_time += timedelta(minutes=5)

    print(f"Generated {readings} temperature readings in {filename}")


if __name__ == '__main__':
    generate_mock_temperature_csv()
