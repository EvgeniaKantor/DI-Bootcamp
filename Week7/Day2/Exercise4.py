from bs4 import BeautifulSoup
from selenium import webdriver
from collections import defaultdict

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

# Navigate to the Technology section of BBC News
url = "https://www.bbc.com/news/technology"
driver.get(url)

# Extract the HTML content after it’s fully loaded
html_content = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')


# Find the desired section
section_outer_6 = soup.find('div', class_= 'sc-2851b0df-0 sc-3e9bbf8-0 kvTVqR jEGMQu')

# Find all headline and date elements within the desired section
headlines = section_outer_6.find_all('h2', class_='sc-4fedabc7-3 zTZri')
dates = section_outer_6.find_all('span', class_='sc-df20d569-1 eGdGwi')

# Extract and print headlines and dates
for headline, date in zip(headlines, dates):
    print(headline.text.strip(), "-", date.text.strip())

# Create a dictionary to categorize articles by publication month
articles_by_month = defaultdict(list)

# Extract and categorize headlines and dates by publication month
for headline, date in zip(headlines, dates):
    # Extract the month from the date
    publication_month = date.text.strip().split()[1]
    # Append the headline and date to the corresponding month in the dictionary
    articles_by_month[publication_month].append((headline.text.strip(), date.text.strip()))

# Print the articles categorized by publication month
for month, articles in articles_by_month.items():
    print(month)
    for headline, date in articles:
        print(f"{headline} - {date}")
    print()