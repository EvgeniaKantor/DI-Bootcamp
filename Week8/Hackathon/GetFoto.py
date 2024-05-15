from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class GetFoto:
    @staticmethod
    def find_most_popular_jackets(df_jackets):
        # Group the data by supplier article and sum up the sales quantity for each article
        popular_jackets = df_jackets.groupby('Supplier Article')['Quantity'].sum()
        # Sort the articles based on their total sales quantity in descending order
        popular_jackets_sorted = popular_jackets.sort_values(ascending=False)
        # Select the top four articles
        top_four_jackets = popular_jackets_sorted.head(4)
        # Initialize a list to store one item code for each supplier article
        unique_item_codes = []
        # Iterate through the top three jackets and select one item code for each supplier article
        for article in top_four_jackets.index:
            # Filter the original DataFrame to get the details of the current supplier article
            article_details = df_jackets[df_jackets['Supplier Article'] == article]
            # Select the first item code encountered for the current supplier article
            unique_item_codes.append(article_details['Item Code'].iloc[0])
        return unique_item_codes

    def fetch_image(self, url, unique_item_code):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        driver = webdriver.Chrome(options=options)

        driver.get(url)
        wait = WebDriverWait(driver, 30)  # Increased wait time to 30 seconds

        # Close the pop-up if it exists
        try:
            pop_up_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cookies__btn')))
            pop_up_button.click()
            print("Closed the pop-up successfully.")
        except:
            print("No pop-up found or error while closing.")

        # Find the image element
        image_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'photo-zoom__preview')))

        # Extract the image URL
        image_url = image_element.get_attribute('src')
        driver.quit()

        # Send a GET request to download the image
        response = requests.get(image_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Specify the file path where you want to save the image
            file_path = f"image_{unique_item_code}.jpg"

            # Save the image to a file
            with open(file_path, "wb") as f:
                f.write(response.content)

            print(f"Image {unique_item_code} saved as {file_path}")
        else:
            print(f"Failed to download image {unique_item_code}")

    def fetch_images_for_top_jackets(self, df_jackets):
        unique_item_codes = self.find_most_popular_jackets(df_jackets)
        # Create URLs for each unique item code
        urls = [f'https://www.wildberries.ru/catalog/{code}/detail.aspx?targetUrl=SP' for code in unique_item_codes]
        # Fetch images for each URL
        for unique_item_code, url in zip(unique_item_codes, urls):
            print(f"Fetching image for item code {unique_item_code}...")
            self.fetch_image(url, unique_item_code)



