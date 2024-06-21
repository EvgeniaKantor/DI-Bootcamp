import requests
from bs4 import BeautifulSoup
import random
import pandas as pd

with open('exercise1.html', 'r') as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
# Find the title of the webpage
title = soup.title.text.strip()
print("Title of the webpage:", title)

# Extract all paragraphs from the page
paragraphs = soup.find_all('p')
print("\nParagraphs on the page:")
for p in paragraphs:
    print(p.text)

# Retrieve all links (URLs in <a href=""> tags) on the page
links = soup.find_all('a')
print("\nLinks on the page:")
for link in links:
    href = link.get('href')
    if href:  # Check if href is not None
        print(href)

#Exercise2  Scraping Robots.Txt From Wikipedia
# URL of the robots.txt file for Wikipedia
url = 'https://en.wikipedia.org/robots.txt'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Limit the text printing to 100 characters
    text = response.text[:100]
    # Print the limited content of the robots.txt file
    print(text)
else:
    # Print an error message if the request failed
    print("Error:", response.status_code)


#Exercise3  Extracting Headers From Wikipedia’s Main Page
# URL of Wikipedia's main page
url = 'https://en.wikipedia.org/wiki/Main_Page'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all header tags (h1, h2, h3, h4, h5, h6)
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # Display the header tags
    for header in headers:
        print('header:\n', header.text.strip())
else:
    # Print an error message if the request failed
    print("Error:", response.status_code)

# Exercise 4 : Checking For Page Title
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title tag
    title_tag = soup.title

    # Check if the title tag exists
    if title_tag:
        print("Page contains a title:", title_tag.text.strip())
    else:
        print("Page does not contain a title")
else:
    # Print an error message if the request failed
    print("Error:", response.status_code)

#Exercise6
#URL of the IMDb list
url = 'https://www.imdb.com/list/ls522499081/?ref_=otl_1'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all divs with class 'lister-item-content'
movie_divs = soup.find_all('div', class_='lister-item-content')

# Extract movie names and years
movie_data = []

# Iterate over each movie div
for movie_div in movie_divs[:50]:  # Get the top 50 movies
    # Extract movie name
    movie_name = movie_div.find('h3').find('a').text.strip()
    # Extract movie year from the span tag with class 'lister-item-year'
    movie_year = movie_div.find('h3').find('a').find_next('span', class_='lister-item-year').text.strip('()')
    # Extract movie index
    movie_index = movie_div.find('span', class_='lister-item-index').text.strip('.')
    # Append movie data to the list
    movie_data.append({'Index': movie_index, 'Name': movie_name, 'Year': movie_year})

# Print the top 10 movies with their indexes
print("Top 10 Movies:")
for movie in movie_data[:10]:
    print(f"{movie['Index']}. {movie['Name']} ({movie['Year']})")

# Create a DataFrame from the movie data
df = pd.DataFrame(movie_data)

# Shuffle the DataFrame
df = df.sample(frac=1)

# Print the shuffled DataFrame
print("\nRandomized Movie DataFrame:")
print(df.head(10))