import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
options = Options()
# options.add_argument('--headless')  # Run in headless mode
# options.add_argument('--ignore-certificate-errors')

# Specify the path to the ChromeDriver
service_obj = Service(executable_path="D:/Darshan/PERSONAL/Python Automation/chromedriver-win64/chromedriver.exe")
# Initialize the Chrome driver
driver = webdriver.Chrome(service=service_obj, options=options)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.instagram.com/")

# Enter username
driver.find_element(By.NAME, "username").send_keys("darshan.patel_7696")
# Enter password
driver.find_element(By.NAME, "password").send_keys("DV05@insta")
# Click on login button
driver.find_element(By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'][1]").click()
time.sleep(7)

wait = WebDriverWait(driver, 10)
# Click on NOT now button
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_ac8f']/div"))).click()

# CLick on NOT NOW button again on home page
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_a9-z']/button[2]"))).click()

# refresh feed
driver.refresh()
driver.find_element(By.XPATH, "//a[text()='darshan.patel_7696']").click()
time.sleep(5)

# checking new messaged if any
driver.back()
wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Messages"]'))).click()
time.sleep(5)

driver.back()
driver.find_element(By.XPATH, "//span[text()='Search']").click()

# search for virat kohli's account
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search input']"))).send_keys("Viral Kohli")

# Click on virat kohli's account
wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Virat Kohli • 269M followers']"))).click()

# Check how much followers virat has ?
followers = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='269M']")))
print(followers.text)
assert followers.text == "269M"

# Check how much follwing virat has ?
following = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="302"]')))
print(following.text)
assert following.text == "302"

# Click on search button on search
time.sleep(5)
driver.close()