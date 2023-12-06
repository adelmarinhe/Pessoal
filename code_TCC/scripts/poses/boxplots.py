import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path_csv = '/code_TCC/analyses/poses/diff_norm/'
path_save = '/code_TCC/analyses/poses/boxplots/'

for j, directory in enumerate(os.listdir(path_csv)):
    data = []
    labels = []  # List to store the names of the plots

    for i, file in enumerate(os.listdir(f'{path_csv}/{directory}')):
        with open(f'{path_csv}/{directory}/{file}', 'r') as csv_file:
            dataframe = pd.read_csv(csv_file)
            data.append(dataframe['error_vector'].tolist())
            labels.append(f'Position {i + 1}')  # Assuming the filename is used as the label

    plt.figure(figsize=(24, 12))
    sns.boxplot(data=data, width=0.5, palette="Set3")

    plt.xlabel('Dataset', fontsize=20)
    plt.ylabel('Error [meters]', fontsize=20)

    plt.xticks(range(len(labels)), labels)

    plt.tick_params(axis='both', labelsize=20)

    if not os.path.isdir(f'{path_save}'):
        os.mkdir(f'{path_save}')

    plt.tight_layout()

    plt.savefig(f'{path_save}/{directory}_boxplot.png')
    plt.close()  # Close the current figure to avoid overlapping plots
