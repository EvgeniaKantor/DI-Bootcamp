from bs4 import BeautifulSoup
from selenium import webdriver
from collections import defaultdict
from collections import Counter
import matplotlib.pyplot as plt

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

# Navigate to the weather forecast page of a specific city
city = "Rehovot"  # Change this to the desired city
url = "https://weather.com/weather/monthly/l/08460724ceb5e9b20ad8ffd2de60bec740b3de6f87d7299caf318aa88a06e939"
driver.get(url)

# Extract the HTML content after it’s fully loaded
html_content = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the desired section
table_weather = soup.find_all('button', class_='CalendarDateCell--dayCell--3ED7m')

# Initialize lists to store the extracted information
dates = []
name_weather = []
high_temp = []
low_temp = []

# Iterate over each element in table_weather to extract the desired information
for table in table_weather:
    # Extract date
    date_elem = table.find('span', class_='CalendarDateCell--date--JO3Db')
    dates.append(date_elem.text if date_elem else "N/A")

    # Extract weather name
    weather_elem = table.find('div', class_='CalendarDateCell--icon--dA6Pp')
    if weather_elem:
        svg_element = weather_elem.find('svg')
        if svg_element:
            name_weather.append(svg_element['name'])

    # Extract high temperature
    high_temp_elem = table.find('div', class_='CalendarDateCell--tempHigh--3k9Yr').find('span', {
        'data-testid': 'TemperatureValue'})
    high_temp.append(high_temp_elem.text if high_temp_elem else "N/A")

    # Extract low temperature
    low_temp_elem = table.find('div', class_='CalendarDateCell--tempLow--2WL7c').find('span', {
        'data-testid': 'TemperatureValue'})
    low_temp.append(low_temp_elem.text if low_temp_elem else "N/A")

# Print the extracted information
for date, weather, high, low in zip(dates, name_weather, high_temp, low_temp):
    print("Date:", date)
    print("Weather:", weather)
    print("High Temp, F:", high)
    print("Low Temp, F:", low)
    print("")

# Convert temperature strings to integers for calculation, handling '--'
high_temp_int = [int(temp.replace('°', '')) for temp in high_temp if temp != '--']
low_temp_int = [int(temp.replace('°', '')) for temp in low_temp if temp != '--']

# Calculate the average high temperature
average_high_temp = sum(high_temp_int) / len(high_temp_int)

# Calculate the average low temperature
average_low_temp = sum(low_temp_int) / len(low_temp_int)

print("Average High Temperature, F:", average_high_temp)
print("Average Low Temperature, F:", average_low_temp)

# Count the occurrences of each weather condition
weather_counts = Counter(name_weather)

# Find the most common weather condition
most_common_weather = weather_counts.most_common(1)[0][0]

print("Most Common Weather Condition:", most_common_weather)

# Count the frequency of each weather condition
weather_counts = defaultdict(int)
for weather in name_weather:
    weather_counts[weather] += 1

# Extract weather conditions and their frequencies
conditions = list(weather_counts.keys())
frequencies = list(weather_counts.values())

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(conditions, frequencies, color='skyblue')
plt.title("Frequency of Weather Conditions in April'24")
plt.xlabel('Weather Condition')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()

# Close the browser
driver.quit()
