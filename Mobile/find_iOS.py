# We don't have apk files so writen below code for only understanding, This might not work as expected.

from appium import webdriver
from appium.webdriver.common.mobileby import mobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))          # This line contains __file__ on which file we're, path.abspath = absulute path of this file and
                                                               # path.dirname = this shows which directory contailns this file

APP = path.join(CUR_DIR, "TheApp.app.zip")              # Contain file path stored in APP veriable

# Start running appium in your local machine from here

APPIUM = 'https://localhost:4743'                       # on 4743 our appium server is running that's why we have mentioned here

CAPS = {
    'plateformname': 'iOS',
    'plateformversion': '13.6',
    'devicename': 'iphone 11',
    'automationname': 'XCUITEST',
    'app': APP
}                                                       # defined capabilities

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)                                                       # Starting browser/App session

try:
    wait = webdriver(driver, 10)
    wait.until(EC.presence_of_element_located(
        (mobileBy.ACCEBILITY_ID, 'login screen')
    ))
    driver.find_element(MobileBy.CLASS_NAME, 'XCUIElementTypeStaticText')
    driver.find_element(MobileBy.XPATH, '//XCUIElementTypeOther[@label='']')
finally:
    driver.quit()                                           # Stopting browser/app session

# python session_iOS.py                                 # Run this command to terminal to appium will start



