# We don't have apk files so writen below code for only understanding, This might not work as expected.

from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))          # This line contains __file__ on which file we're, path.abspath = absulute path of this file and
                                                               # path.dirname = this shows which directory contailns this file

APP = path.join(CUR_DIR, "TheApp.app")              # Contain file path stored in APP veriable

# Start running appium in your local machine from here

APPIUM = 'https://localhost:4743'                       # on 4743 our appium server is running that's why we have mentioned here

CAPS = {
    'plateformname': 'Android',
    'devicename': 'Android Emulator',
    'automationname': 'UIAutomator2',
    'app': APP
}                                                       # defined capabilities
                                                        # If you want your script will run on all version then remove 'plateformversion': '13.6'

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)                                                       # Starting browser/App session

driver.quit()                                           # Stopting browser/app session

# python session_Android.py                                 # Run this command to terminal to appium will start



