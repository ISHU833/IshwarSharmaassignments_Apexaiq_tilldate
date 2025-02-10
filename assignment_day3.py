# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Open the page
driver.get("https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info")
time.sleep(2)

# Function to extract table data dynamically
def extract_table_data(table_xpath):
    table = driver.find_element(By.XPATH, table_xpath)
    rows = table.find_elements(By.XPATH, ".//tbody//tr")
    
    # Extract header
    header_row = table.find_elements(By.XPATH, ".//thead//tr/th")
    headers = [header.text for header in header_row]
    
    list_of_rows = []
    
    for row in rows:
        columns = row.find_elements(By.XPATH, ".//td")
        row_data = [col.text for col in columns]
        if row_data:  # Append only non-empty rows
            list_of_rows.append(row_data)
    
    # Return both headers and rows
    return headers, list_of_rows

# Extract first table
header_1, list_of_rows1 = extract_table_data("//*[@id='winrelinfo_container']/div[2]/table")
df1 = pd.DataFrame(list_of_rows1, columns=header_1)
df1.to_csv("first_table.csv", index=False)
print("First Table:")
print(df1)

# Extract second table
header_2, list_of_rows2 = extract_table_data("//*[@id='historyTable_0']")
df2 = pd.DataFrame(list_of_rows2, columns=header_2)
df2.to_csv("second_table.csv", index=False)
print("Second Table:")
print(df2)

# Close the WebDriver
driver.quit()
