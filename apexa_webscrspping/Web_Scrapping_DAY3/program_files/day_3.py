
# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chromedriver_path="D:/apexa_webscrspping/program_files/chromedriver-win64/chromedriver.exe"
service = Service(chromedriver_path)

Options=Options()
Options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=Options)
driver.maximize_window()
driver.get("https://www.google.co.uk/")
print(driver.title)

input = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")
input.send_keys("Linkldin")
time.sleep(1)

search = driver.find_element(By.XPATH, "//input[@name='btnK']")
search.click()
# driver.quit()