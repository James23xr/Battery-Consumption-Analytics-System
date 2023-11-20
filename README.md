# Battery-Consumption-Analytics-System


## Introduction

This Python script is designed to monitor and analyze the battery life of a device over time. It logs the battery percentage at regular intervals and provides a visual representation of battery consumption. This tool is useful for understanding battery usage patterns and identifying potential issues with battery life.

## Features

- **Battery Status Logging:** Logs battery percentage at predefined intervals.
- **Data Storage:** Stores battery status data with timestamps in a structured format.
- **Data Analysis:** Converts logged data into a pandas DataFrame for easy analysis.
- **Visualization:** Plots battery percentage over time to visually analyze battery consumption.

## Installation

To run this script, you will need to install the following Python libraries:
- `psutil`: For accessing battery information.
- `pandas`: For data handling and analysis.
- `matplotlib`: For plotting the battery data.

These can be installed via pip:
```bash
pip install psutil pandas matplotlib
```

## Usage

1. **Running the Script:** Execute the script to start logging battery data.
2. **Data Logging:** The script logs the current battery percentage at intervals defined by `SAMPLING_INTERVAL`.
3. **Interrupting the Logging:** Use Ctrl+C (KeyboardInterrupt) to stop data logging.
4. **Data Visualization:** After stopping the logging, a plot will be displayed showing the battery percentage over time.

## Configuration

- **SAMPLING_INTERVAL:** Set the time interval (in seconds) for how often you want to log the battery status. Default is set to 3600 seconds (1 hour).

## Extending the Application

- **Custom Intervals:** Adjust `SAMPLING_INTERVAL` for more or less frequent logging.
- **Additional Metrics:** Expand the script to log more battery-related metrics like power source, time remaining, etc.
- **Data Export:** Implement functionality to export the logged data to a file (e.g., CSV) for long-term analysis.
- **Alerts:** Add a feature to send alerts when the battery reaches certain levels.

## Notes

- The script is intended for educational and analytical purposes and is not a full-fledged battery management tool.
- Battery information accuracy depends on the `psutil` library and the underlying system hardware.

## License

This project is open-source and free to use or modify.
