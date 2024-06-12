from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Load your DataFrame
df_top_amazon = pd.read_excel('df_top_amazon_v5.xlsx')  # Assuming the file extension is .xlsx


def fetch_info(driver, url):
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 30)  # Increased wait time to 30 seconds

        # Find and click the button
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#askATFLink")))
        search_button.click()
        time.sleep(2)  # Wait for the content to load

        # Extract the required information
        content = driver.find_element(By.CSS_SELECTOR, "p.a-spacing-small span").text
        return content
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return None


# Initialize the WebDriver once
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Uncomment to run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Apply the function to each URL and create a new column with the extracted information
df_top_amazon['short_feedback'] = df_top_amazon['product_url'].apply(lambda x: fetch_info(driver, x))

# Close the WebDriver
driver.quit()

# Display the updated DataFrame
print(df_top_amazon)

# Optionally, save the updated DataFrame to a new file
df_top_amazon.to_excel('df_top_amazon_with_feedback.xlsx', index=False)

