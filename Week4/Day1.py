import pandas as pd

data = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}

df = pd.DataFrame(data)
print("First few rows of the DataFrame:")
print(df.head())

print("Statistical summary:")
print(df.describe())

print("Concise summary of the DataFrame:")
print(df.info())

print("Sort the DataFrame:")
print(df.sort_values(by='Price'))

print("Filter the books by a specific Genre or books with Price above a certain threshold:")
print(df[df['Genre'] == 'Classic'])
print(df[df['Price'] > 10])

print("Group the books by Author and sum up the Copies Sold:")
print(df.groupby('Author')['Copies Sold'].sum())
#