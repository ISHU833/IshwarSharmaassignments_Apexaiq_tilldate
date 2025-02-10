from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd 
import time

# chromedriver_path = "D:\apexa_webscrspping\program_files\chromedriver-win64\chromedriver.exe"
# service = Service(chromedriver_path)

# options = Options()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info")
time.sleep(1)

table = driver.find_element(By.XPATH, "//*[@id='winrelinfo_container']/div[2]/table")
header_elements = table.find_elements(By.XPATH, ".//tbody//th")
headers = []

for header in header_elements:
    headers.append(header.text)
print("Headers:", headers)

rows = table.find_elements(By.XPATH, ".//tbody//tr")
data = []

for row in rows:
    row_data = []
    cells = row.find_elements(By.XPATH, ".//td")
    for cell in cells:
        row_data.append(cell.text)
    data.append(row_data)
print("Data:", data)

df = pd.DataFrame(data, columns=headers if headers else None)
df.to_csv("extracted_table.csv", index=False)
print(df)
driver.quit()

    