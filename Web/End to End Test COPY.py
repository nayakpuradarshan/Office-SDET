import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chromedriver setup
service_obj = Service(executable_path="D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Impicit wait and maximize wait
driver.implicitly_wait(7)
driver.maximize_window()

# get this url on browser
driver.get("https://rahulshettyacademy.com/angularpractice/")

#  //a[contains(@href,'shop')]    a[href*='shop']
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()

# find this element and stored in variable
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products :
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successText

time.sleep(3)
driver.close()

