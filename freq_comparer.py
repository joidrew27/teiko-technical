import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv('cell-count.csv')

# Filter data
filtered_data = df[(df['treatment'] == 'tr1') & (df['sample_type'] == 'PBMC') & (df['condition'] == 'melanoma')]

# Group data by response
grouped_data = filtered_data.groupby('response')
print(grouped_data.describe())

# List of immune cell populations
cell_populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

# Create boxplots
for population in cell_populations:
    plt.figure(figsize=(8, 6))
    # Create a box plot for each group
    plt.boxplot(grouped_data.describe()[population].transpose(), labels=['Responder', 'Non-Responder'])
    plt.ylabel('Cell number')
    plt.title(f'{population} Relative Frequencies for Responders vs. Non-Responders')
    plt.show()
