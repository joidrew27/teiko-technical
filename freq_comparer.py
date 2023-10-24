import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the CSV data
df = pd.read_csv('cell-count.csv')

# Filter data
filtered_data = df[(df['treatment'] == 'tr1') & (df['sample_type'] == 'PBMC') & (df['condition'] == 'melanoma')]

# Group data by response
grouped_data = filtered_data.groupby('response')

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
    
    # Separate data for responders and non-responders
    responders_data = grouped_data.describe()[population].transpose()['y'] # Data for responders for a specific cell population
    non_responders_data = grouped_data.describe()[population].transpose()['n'] # Data for non-responders for the same cell population

    # Perform a two-sample t-test
    t_stat, p_value = stats.ttest_ind(responders_data, non_responders_data)

    # Check if the p-value is significant
    if p_value < 0.05:
        print("There is a significant difference between responders and non-responders for " + population)
    else:
        print("There is no significant difference between responders and non-responders for " + population)


