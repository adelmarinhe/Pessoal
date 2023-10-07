JSON_FILES_FOLDER_PATH = "C:/Users/jams/Documents/Pessoal/code_TCC/json_data_files"
CSV_FILES_FOLDER = "C:/Users/jams/Documents/Pessoal/code_TCC/csv_data_files"
PLOTS_FOLDER = "C:/Users/jams/Documents/Pessoal/code_TCC/plots"

actuator_attributes = ['commandId', 'statusFlags', 'jitterComm', 'position', 'velocity', 'torque',
                       'currentMotor', 'voltage', 'temperatureMotor', 'temperatureCore', 'faultBankA',
                       'faultBankB', 'warningBankB', 'warningBankB']

sequence = [f'movement_2_safe_grasp', f'movement_3_grasp', f'movement_2_safe_grasp', f'movement_4_safe_release',
            f'movement_5_release', f'movement_4_safe_release', 'Home']

movements = {f'movement_{i + 1}': sequence[i] for i in range(7)}

expected_joint_angles = {'movement_1': ['movement_2_safe_grasp', [22.690292358398438,
                                                                  347.787841796875,
                                                                  91.1580810546875,
                                                                  345.40728759765625,
                                                                  300.799072265625,
                                                                  352.2476806640625]],
                         'movement_2': ['movement_3_grasp', [36.26722717285156,
                                                             336.98724365234375,
                                                             85.48641967773438,
                                                             350.34735107421875,
                                                             314.64813232421875,
                                                             350.21044921875]],
                         'movement_3': ['movement_2_safe_grasp', [22.690292358398438,
                                                                  347.787841796875,
                                                                  91.1580810546875,
                                                                  345.40728759765625,
                                                                  300.799072265625,
                                                                  352.2476806640625]],
                         'movement_4': ['movement_4_safe_release', [7.6923065185546875,
                                                                    293.3585205078125,
                                                                    36.652435302734375,
                                                                    270.0581359863281,
                                                                    283.05670166015625,
                                                                    97.69122314453125]],
                         'movement_5': ['movement_5_release', [7.6994171142578125,
                                                               288.1332702636719,
                                                               38.8013916015625,
                                                               270.02423095703125,
                                                               290.4320068359375,
                                                               97.71112060546875]],
                         'movement_6': ['movement_4_safe_release', [7.6923065185546875,
                                                                    293.3585205078125,
                                                                    36.652435302734375,
                                                                    270.0581359863281,
                                                                    283.05670166015625,
                                                                    97.69122314453125]],
                         'movement_7': ['Home', [0, 344, 75, 0, 300, 0]]}
