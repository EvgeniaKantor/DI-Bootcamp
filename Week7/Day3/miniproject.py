from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

url = 'https://www.inmotionhosting.com/'
driver.get(url)

# Wait for the pop-up to appear and close it
wait = WebDriverWait(driver, 10)
pop_up = wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-close-btn-container')))
pop_up.click()

# Find and click on the "Shared Hosting Plans" link
link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Shared Hosting Plans')))
link.click()

# Wait for the "Compare Plans" button to be clickable
compare_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="shared-hosting-spec-table"]/div/div[1]/button[4]')))
compare_button.click()

# Wait for the table to load
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shared-hosting-spec-table"]/div/div[2]/table')))

# Find all rows in the table
rows = driver.find_elements(By.XPATH, '//*[@id="shared-hosting-spec-table"]/div/div[2]/table/tbody/tr')

table_list = []
for row in rows:
    try:
        # Extract tooltips value for each row
        tooltips = row.find_element(By.CLASS_NAME, 'tooltips-table').text.strip()
    except:
        tooltips = None

    # Extract plan data
    cells = row.find_elements(By.TAG_NAME, 'td')
    plan_data = []
    for cell in cells:
        if cell.get_attribute('class') == 'check':
            plan_data.append('Yes')
        elif cell.get_attribute('class') == 'dash':
            plan_data.append('No')
        else:
            plan_data.append(cell.text.strip() if cell.text.strip() != '' else None)

    if len(plan_data) == 5:  # Check if the row has the expected number of cells
        table_item = {
            'Tooltips': tooltips,
            'Core': plan_data[1],
            'Launch': plan_data[2],
            'Power': plan_data[3],
            'Pro': plan_data[4]
        }
        table_list.append(table_item)

df = pd.DataFrame(table_list)
print(df)

# Close the Selenium WebDriver
driver.quit()


