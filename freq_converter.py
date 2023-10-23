import pandas as pd

# Load the input CSV file
df = pd.read_csv('cell-count.csv')

# Calculate the total cell count for each sample (row)
df['total_count'] = df[['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']].sum(axis=1)

# Iterate through each row in the input DataFrame
for index, row in df.iterrows():
    sample = row['sample']
    total_count = row['total_count']
    
    # Create an empty DataFrame to store the results as specified by following:
        # sample: the sample id as in column sample in cell-count.csv
        # total_count: total cell count of sample
        # population: name of the immune cell population (e.g. b_cell, cd8_t_cell, etc.)
        # count: cell count
        # percentage: relative frequency in percentage
    results = pd.DataFrame(columns=['sample', 'total_count', 'population', 'count', 'percentage'])

    # Iterate through the five populations
    for population in ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']:
        count = row[population]
        percentage = (count / total_count) * 100
        
        # Append a new row to the results DataFrame
        new_row = {'sample': sample, 'total_count': total_count, 'population': population, 'count': count, 'percentage': percentage}
        results = results._append(new_row, ignore_index=True)

        # Save the results to an output CSV file
        output_file = 'cell-frequency-sample-{}.csv'.format(sample)
        results.to_csv(output_file, index=False)
