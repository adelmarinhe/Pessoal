import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('2023-08-24_actuator_6.csv')

# Extract relevant data
timestamps = data['Timestamp']
values = data['Column_6']  # Change this to the appropriate column name

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(timestamps, values, marker='o')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Data Plot')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
