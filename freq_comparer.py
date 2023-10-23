import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load the CSV data
df = pd.read_csv('cell-count.csv')

# Filter data
filtered_data = df[(df['treatment'] == 'tr1') & (df['sample_type'] == 'PBMC')]

# Group data by response
grouped_data = filtered_data.groupby('response')

# List of immune cell populations
cell_populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

# Create boxplots
for population in cell_populations:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='response', y=population, data=grouped_data)
    plt.title(f'{population} Relative Frequencies for Responders vs. Non-Responders')
    plt.show()

    # Perform statistical test
    responders = grouped_data.get_group('y')[population]
    non_responders = grouped_data.get_group('n')[population]

    t_stat, p_value = ttest_ind(responders, non_responders)
    print(f'Statistical Test for {population}: t-statistic = {t_stat}, p-value = {p_value}')
