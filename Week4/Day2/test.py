import numpy as np
from faker import Faker
import pandas as pd

fake = Faker()

# Generating synthetic sales data
sales_data = [(fake.word(), np.random.randint(10, 500), fake.date_this_year(), np.random.randint(18, 70)) for _ in range(500)]
sales_df = pd.DataFrame(sales_data, columns=['Product', 'Sale Amount', 'Date', 'Customer Age'])

# Display the first few rows of the DataFrame
print(sales_df.head())