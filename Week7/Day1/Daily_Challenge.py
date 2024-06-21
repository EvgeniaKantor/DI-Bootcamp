import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the GitHub Topics page
url = 'https://github.com/topics'

# Send a GET request to the URL
response = requests.get(url)

# Verify the request was successful (status code 200)
if response.status_code == 200:
    # Print the first 100 characters of the HTML content
    print("First 100 characters of HTML content:")
    print(response.text[:100])
    # Print the status code of the response
    print("Status Code:", response.status_code)

    # Save the HTML content to a file named webpage.html
    with open('webpage.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
else:
    print("Failed to retrieve data from the URL.")

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
# Find all divs with class 'py-4 border-bottom d-flex flex-justify-between'
topics_divs = soup.find_all('div', class_='py-4 border-bottom d-flex flex-justify-between')
# Extract topic names and descriptions
topics_data = []
for topic_div in topics_divs:
    topic_name = topic_div.find('p', class_='f3 lh-condensed mb-0 mt-1 Link--primary').text.strip()
    topic_description = topic_div.find('p', class_='f5 color-fg-muted mb-0 mt-1').text.strip()
    topics_data.append({'Name': topic_name, 'Description': topic_description})

# Print the length and content of each extracted list
print("\nNumber of topics extracted:", len(topics_data))
print("Topics extracted:", topics_data)

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(topics_data)

# Print the DataFrame to confirm its structure and contents
print("\nDataFrame:")
print(df)