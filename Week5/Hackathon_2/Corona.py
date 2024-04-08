import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Convert the 'Day' column to datetime
data['Day'] = pd.to_datetime(data['Day'])
# Filter the data for doses administered for all vaccines
vaccines_data = data[['Pfizer/BioNTech', 'Moderna', 'Oxford/AstraZeneca', 'Johnson&Johnson',
                      'Sputnik V', 'Sinovac', 'Novavax', 'Covaxin', 'Sanofi/GSK', 'Valneva']]

# Group the filtered data by year and sum the doses administered for each vaccine
yearly_doses = vaccines_data.groupby(data['Day'].dt.year).sum()

# Display the table
print('Yearly_does: ', yearly_doses)
#########################################################################
# Create a heatmap for visualizing the doses administered for each vaccine over time
plt.figure(figsize=(12, 8))
sns.heatmap(yearly_doses.T, cmap='YlGnBu', annot=True, fmt=',.0f')
plt.title('Doses Administered for Each Vaccine Over Time')
plt.xlabel('Year')
plt.ylabel('Vaccine')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
############################################################################
# Define custom colors
colors = ['#FFFF00', '#87CEEB', '#90EE90']

# Plotting the overall graph
plt.figure(figsize=(10, 6))

# Plotting Pfizer/BioNTech doses
plt.plot(yearly_doses.index, yearly_doses['Pfizer/BioNTech'], marker='o', linestyle='-', color=colors[1], label='Pfizer/BioNTech, Germany')

# Plotting Moderna doses
plt.plot(yearly_doses.index, yearly_doses['Moderna'], marker='o', linestyle='-', color=colors[2], label='Moderna, United States')

# Plotting Oxford/AstraZeneca doses
plt.plot(yearly_doses.index, yearly_doses['Oxford/AstraZeneca'], marker='o', linestyle='-', color=colors[0], label='Oxford/AstraZeneca, England and Swedish')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Total Doses Administered')
plt.title('Vaccines Administered by Year')
plt.legend()

# Displaying the plot
plt.grid(True)
plt.tight_layout()
plt.show()

# # Group the data by country and year and sum the Pfizer/BioNTech doses
# pfizer_by_country = data.groupby(['Entity', data['Day'].dt.year])['Pfizer/BioNTech'].sum()
# moderna_by_country = data.groupby(['Entity', data['Day'].dt.year])['Moderna'].sum()
# oxford_by_country = data.groupby(['Entity', data['Day']])['Oxford/AstraZeneca'].sum()
#
#
# pfizer_by_country_df = pfizer_by_country.reset_index()
# moderna_by_country_df = moderna_by_country.reset_index()
# oxford_by_country_df = oxford_by_country.reset_index()
