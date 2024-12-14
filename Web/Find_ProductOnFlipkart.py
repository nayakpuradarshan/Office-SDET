import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# initializing drivers
service_obj = Service("D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# applied implicit wait and maximize page
driver.implicitly_wait(10)
driver.maximize_window()

# get the url
driver.get("https://www.flipkart.com/")

# search driver title
print(driver.title)

try:
    if driver.title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!":
        print("Right title")
except:
    print("Wrong title")

driver.find_element(By.NAME, "q").click()
driver.find_element(By.NAME, "q").send_keys("Macbook air m2")
time.sleep(2)
driver.find_element(By.NAME, "q").send_keys(Keys.RETURN)
time.sleep(5)

wait = WebDriverWait(driver, 10)

#  Close driver
driver.close()