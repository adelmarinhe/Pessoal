import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

from code_TCC.scripts import utils

csv_path = utils.CSV_FILES_FOLDER
plots_path = utils.PLOTS_FOLDER
movements = utils.movements

actuator_attributes_interest = ['position', 'velocity', 'torque', 'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore']

for directory in os.listdir(csv_path):
    for file in os.listdir(f'{csv_path}/{directory}'):
        with open(f'{csv_path}/{directory}/{file}', 'r') as csv_file:
            dataframe = pd.read_csv(csv_file)

            date = f'{directory}'
            actuator = f'{file}'

            for movement in movements:
                filtered_df = dataframe[dataframe['Movement'] == movement]

                # Specify the figsize parameter to set a larger plot size
                fig, ax = plt.subplots(figsize=(20, 10))  # Adjust the width and height as needed

                time_format = "%H:%M:%S"
                datetime_timestamps = [datetime.strptime(ts, time_format) for ts in filtered_df['Time']]

                ax.plot(datetime_timestamps, filtered_df['position'], label='Position')

                ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

                ax.set_xlabel('Time')
                ax.set_ylabel('Value')
                ax.set_title(f'Time Series Plot of the positional data of {actuator} for {movement} in {date}')

                ax.legend()

                if not os.path.isdir(f'{plots_path}/{date}'):
                    os.mkdir(f'{plots_path}/{date}')

                if not os.path.isdir(f'{plots_path}/{date}/{actuator}'):
                    os.mkdir(f'{plots_path}/{date}/{actuator}')

                plt.savefig(f'{plots_path}/{date}/{actuator}/{date}_{actuator}_{movement}.png')
