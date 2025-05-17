# Structural-Health-Monitoring-System-NM


📘 Introduction

Structural Health Monitoring (SHM) is a critical process for ensuring the safety, durability, and functionality of infrastructure such as bridges, buildings, and tunnels. The proposed system simulates real-time monitoring of structural parameters including strain, vibration, and temperature. By analyzing these parameters, it helps identify anomalies or signs of deterioration, thereby enabling preventive maintenance and reducing the risk of catastrophic failures.


🎯 Objective

To simulate real-time structural health data (strain, vibration, temperature).

To analyze the data against defined safety thresholds.

To generate alerts when abnormal values are detected.

To visualize patterns and anomalies for decision-making.

To build a lightweight prototype using Python and basic data visualization tools.


📊 Data Source

This project uses simulated sensor data generated through Python's random.uniform() function to emulate:

Strain in microstrain units.

Vibration in g-force.

Temperature in degrees Celsius.

In a real-world application, these values would be collected from actual sensors installed on infrastructure components.


📈 Visualization

Although the current version prints sensor values and alerts in the terminal, you can extend it using:

Matplotlib or Seaborn for line plots or heatmaps.

Plotly for interactive dashboards.

CSV logging for tracking long-term trends.


🛠 Technologies Used
Python 3.x

Standard libraries:

random – for simulating sensor data

time – to simulate real-time intervals

Optional (for visualization):

matplotlib

pandas

seaborn


▶️ How to Run

1. Clone the repository

2. Install dependencies

3. Run the program



