import pandas as pd
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def extract_table(url):
    """Extracts a table from the given URL and returns it as a Pandas DataFrame.

    Args:
        url: The URL of the page containing the table.

    Returns:
        A Pandas DataFrame containing the table data.
    """

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless') # Ensure GUI is off
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Set up the WebDriver
    # Adjust the path to chromedriver if necessary
    service = Service('/usr/lib/chromium-browser/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the webpage
        driver.get(url)

        # Wait for the table to be present on the page
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.table')))  # Adjust the selector as needed

        # Extract table headers
        headers = [th.text for th in table.find_elements(By.TAG_NAME, 'th')]

        # Extract table rows
        rows = []
        for row in table.find_elements(By.TAG_NAME, 'tr'):
            cells = [cell.text for cell in row.find_elements(By.TAG_NAME, 'td')]
            rows.append(cells)

        # Create Pandas DataFrame
        df = pd.DataFrame(rows, columns=headers)

    finally:
        # Close the WebDriver
        driver.quit()

    return df

# Example usage
url = 'https://josaa.admissions.nic.in/Applicant/seatallotmentresult/currentorcr.aspx'  # Replace with the actual URL
df = extract_table(url)
print(df)