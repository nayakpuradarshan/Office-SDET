import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initializing driver
service_obj = Service(executable_path="D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# applied implicit wait for 10 seconds and maximize page
driver.maximize_window()
driver.implicitly_wait(10)

# Open mentioned url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))

count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").click()
driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").clear()
driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")

# driver.find_element(By.XPATH, '//button[@class="promoBtn"]').click()
# driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="promoBtn"]'))).click()
time.sleep(5)

#Total Amount
TotalAmount = int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)

# Total After Discount
TotalAfterDiscount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

time.sleep(5)
assert TotalAmount > TotalAfterDiscount
time.sleep(5)

print("Success!")
driver.close()