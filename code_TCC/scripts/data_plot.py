import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

JSON_FILES_FOLDER = "json_data_files"
CSV_FILES_FOLDER = "csv_data_files"
PLOTS_FOLDER = "plots"

movements = ['Time4_safe_remedio1', 'Time4_remedio1', 'Time4_soltar_remedio', 'Time4_caixinha', 'Home']
actuator_attributes_interest = ['position', 'velocity', 'torque', 'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore']

for file in os.listdir(CSV_FILES_FOLDER):
    with open(f'{CSV_FILES_FOLDER}/{file}', 'r') as csv_file:
        dataframe = pd.read_csv(csv_file)

        date = file.split("_")[0]
        actuator = file.split("_")[1].split(".")[0]

        for movement in movements:
            filtered_df = dataframe[dataframe['Movement'] == movement]

            fig, ax = plt.subplots()

            time_format = "%H:%M:%S"
            datetime_timestamps = [datetime.strptime(ts, time_format) for ts in filtered_df['Time']]

            ax.plot(datetime_timestamps, filtered_df['position'], label='Position')

            ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

            ax.set_xlabel('Time')
            ax.set_ylabel('Value')
            ax.set_title(f'Time Series Plot of the positional data of {actuator} for {movement} in {date}')

            ax.legend()

            if not os.path.isdir(f'{PLOTS_FOLDER}/{date}'):
                os.mkdir(f'{PLOTS_FOLDER}/{date}')

            plt.savefig(f'{PLOTS_FOLDER}/{date}/{date}_{actuator}_{movement}.png')

