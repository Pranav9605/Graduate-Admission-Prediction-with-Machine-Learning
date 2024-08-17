# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()



# Install required packages
# In VSCode, you'll typically run these commands in the terminal
# pip install selenium
# sudo apt-get update
# sudo apt-get install -y chromium-chromedriver chromium-browser


#---------------------------------------------------------------------------------------------



# import pandas as pd
# import os
# import sys
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# import time

# def extract_table(url):
#     """Extracts a table from the given URL and returns it as a Pandas DataFrame.

#     Args:
#         url: The URL of the page containing the table.

#     Returns:
#         A Pandas DataFrame containing the table data.
#     """

#     # Set up Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument('--headless') # Ensure GUI is off
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')

#     # Set up the WebDriver
#     # Adjust the path to chromedriver if necessary
#     service = Service('C:\\Users\\Pranav padmanabhan\\Downloads\\chromedriver-win64\\chromedriver.exe')
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     try:
#         # Open the webpage
#         driver.get(url)
#         time.sleep(5)

#         # Wait for the table to be present on the page
#         wait = WebDriverWait(driver, 10)
#         table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.table')))  # Adjust the selector as needed

#         # Extract table headers
#         headers = [th.text for th in table.find_elements(By.TAG_NAME, 'th')]

#         # Extract table rows
#         rows = []
#         for row in table.find_elements(By.TAG_NAME, 'tr'):
#             cells = [cell.text for cell in row.find_elements(By.TAG_NAME, 'td')]
#             rows.append(cells)

#         # Create Pandas DataFrame
#         df = pd.DataFrame(rows, columns=headers)

#     finally:
#         # Close the WebDriver
#         driver.quit()

#     return df

# # Example usage
# url = 'https://josaa.admissions.nic.in/Applicant/seatallotmentresult/currentorcr.aspx'  # Replace with the actual URL
# df = extract_table(url)

# print(df)







# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# time.sleep(10)









#--------------------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
import time

def extract_table(url):
    """Extracts a table from the given URL and returns it as a Pandas DataFrame.

    Args:
        url: The URL of the page containing the table.

    Returns:
        A Pandas DataFrame containing the table data.
    """
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--enable-javascript')
    chrome_options.add_argument('--window-size=1920,1080')

    # Specify the path to the ChromeDriver
    service = Service(r'C:\Users\Pranav padmanabhan\Downloads\chromedriver-win64\chromedriver.exe')
    
    # Set up the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the webpage
        driver.get(url)

        # Wait for the page to load completely
        time.sleep(10)  # Increase this value if necessary

        # Check if the 'Sys' error exists and reload the page if necessary
        if "Sys is not defined" in driver.page_source:
            driver.refresh()
            time.sleep(20)

        # Wait for the table to be present on the page
        wait = WebDriverWait(driver, 15)
        # Wait for the specific table to be present on the page
        # Wait for the specific table using XPath
        table = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_GridView1"]')))

  # Adjust the selector as needed

        # Extract table headers
        headers = [th.text for th in table.find_elements(By.TAG_NAME, 'th')]

        # Extract table rows
        rows = []
        for row in table.find_elements(By.TAG_NAME, 'tr'):
            cells = [cell.text for cell in row.find_elements(By.TAG_NAME, 'td')]
            if cells:  # Only append non-empty rows
                rows.append(cells)

        # Create Pandas DataFrame
        df = pd.DataFrame(rows, columns=headers)

    except TimeoutException:
        print("Timed out waiting for the table to load. The table might not be present or the selector could be incorrect.")
        df = pd.DataFrame()  # Return an empty DataFrame in case of failure

    finally:
        # Close the WebDriver
        driver.quit()

    return df

# Example usage
if __name__ == "__main__":
    url = 'https://josaa.admissions.nic.in/applicant/SeatAllotmentResult/CurrentORCR.aspx'  # Replace with the actual URL
    df = extract_table(url)
    print(df)
