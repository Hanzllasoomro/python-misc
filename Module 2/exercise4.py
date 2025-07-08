# Threading
#  EXERCISE – 4
# • Youare required to conduct analysis on data obtained from a plant related to temperature
# readings.
#  • Thefile temperatures.csv contains the appropriate data required for this task.
#  • Write methods to generate:
#  • Average time lapse in readings
#  • Average per hour temperature recording
#  • Largest spike in data (percentage)
#  • Overall deviation in the data
#  • Conduct the above calculations through two threads (each thread conducts two calculations).
#  • Measure uptime with and without threads. Log your results in section_four/temperature.txt
#  using the appropriate library.

import csv
import threading
import time
import os
from datetime import datetime
from statistics import mean, stdev
from collections import defaultdict

# Create output directory
os.makedirs("section_four", exist_ok=True)

# Read CSV and parse data
def read_temperature_data(filename):
    timestamps = []
    temperatures = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            timestamps.append(datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S'))
            temperatures.append(float(row['temperature']))
    return timestamps, temperatures

# Analysis functions
def average_time_lapse(timestamps):
    lapses = [(timestamps[i+1] - timestamps[i]).total_seconds() for i in range(len(timestamps)-1)]
    return mean(lapses)

def average_per_hour(timestamps, temperatures):
    hour_map = defaultdict(list)
    for ts, temp in zip(timestamps, temperatures):
        hour_map[ts.hour].append(temp)
    return {hour: mean(temps) for hour, temps in hour_map.items()}

def largest_spike(temperatures):
    spikes = [(abs(temperatures[i+1] - temperatures[i]) / temperatures[i]) * 100
              for i in range(len(temperatures)-1) if temperatures[i] != 0]
    return max(spikes)

def temperature_deviation(temperatures):
    return stdev(temperatures)

# Thread target functions
def thread_1(timestamps, temperatures, results):
    results['avg_lapse'] = average_time_lapse(timestamps)
    results['avg_hourly'] = average_per_hour(timestamps, temperatures)

def thread_2(timestamps, temperatures, results):
    results['spike'] = largest_spike(temperatures)
    results['deviation'] = temperature_deviation(temperatures)

# Run with threading
def run_with_threads(timestamps, temperatures):
    results = {}
    t1 = threading.Thread(target=thread_1, args=(timestamps, temperatures, results))
    t2 = threading.Thread(target=thread_2, args=(timestamps, temperatures, results))
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    elapsed = time.time() - start
    return results, elapsed

# Run without threading
def run_without_threads(timestamps, temperatures):
    results = {}
    start = time.time()
    thread_1(timestamps, temperatures, results)
    thread_2(timestamps, temperatures, results)
    elapsed = time.time() - start
    return results, elapsed

# Save results to file
def save_results(results_with_threads, time_with_threads, results_without_threads, time_without_threads):
    with open("section_four/temperature.txt", "w") as f:
        f.write("=== With Threads ===\n")
        for key, value in results_with_threads.items():
            f.write(f"{key}: {value}\n")
        f.write(f"Execution Time: {time_with_threads:.4f} seconds\n\n")

        f.write("=== Without Threads ===\n")
        for key, value in results_without_threads.items():
            f.write(f"{key}: {value}\n")
        f.write(f"Execution Time: {time_without_threads:.4f} seconds\n")

# Main
def main():
    timestamps, temperatures = read_temperature_data("temperatures.csv")
    results_with_threads, time_with_threads = run_with_threads(timestamps, temperatures)
    results_without_threads, time_without_threads = run_without_threads(timestamps, temperatures)
    save_results(results_with_threads, time_with_threads, results_without_threads, time_without_threads)
    print("Analysis complete. Results saved to section_four/temperature.txt")

if __name__ == "__main__":
    main()
