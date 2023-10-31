import psutil
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Define how often you want to check the battery status (e.g., every hour)
SAMPLING_INTERVAL = 3600  # seconds

# To store battery data
battery_data = []

def log_battery_status():
    battery = psutil.sensors_battery()
    timestamp = datetime.datetime.now()
    
    # Store percentage and timestamp
    battery_data.append({
        "timestamp": timestamp,
        "percentage": battery.percent
    })
    print(f"Logged at {timestamp}: {battery.percent}%")

def main():
    try:
        while True:
            log_battery_status()
            time.sleep(SAMPLING_INTERVAL)
    except KeyboardInterrupt:
        print("\nLogging stopped by user.")

    # Convert data to DataFrame for analysis
    df = pd.DataFrame(battery_data)

    # Calculate hours since start for better x-axis labeling
    start_time = df['timestamp'].iloc[0]
    df['hours_since_start'] = df['timestamp'].apply(lambda x: (x - start_time).seconds / 3600)

    # Plotting battery consumption over hours since start
    plt.figure(figsize=(10, 6))
    plt.plot(df['hours_since_start'], df['percentage'], '-o', label='Battery Percentage')
    plt.xlabel('Hours Since Start')
    plt.ylabel('Battery Percentage')
    plt.title('Battery Consumption Over Hours')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
