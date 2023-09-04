from selenium import webdriver
import glob
from pathlib import Path
import time
import os
from datetime import datetime

class AttendanceCapture(object):

  def execureSteps(self, data):
    # chromeOptions = webdriver.ChromeOptions()
    # prefs = {"download.default_directory": Path}
    # chromeOptions.add_experimental_option("prefs", prefs)
    # chromeOptions.add_argument("window-size=1920,1080")
    # chromeOptions.add_argument("--headless")
    # chromeOptions.add_argument('--no-sandbox')
    # chromeOptions.add_argument('--disable-dev-shm-usage')
    # chromeOptions.add_argument("--remote-debugging-port=9222")

    # if you getting driver error then download new driver for latest crome, as crome keep getting updated, so does the driver
    # version of driver and crome should always be same
    # https://chromedriver.chromium.org/downloads

    options = webdriver.ChromeOptions()
    options.headless = True
    options.no_sandbox = True
    options.shm = True
    options._debugger_address = '0.0.0.0:9222'

    chrome_options = webdriver.ChromeOptions()
    # prefs = {"download.default_directory": Path}
    # chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("window-size=1920,1080")

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--remote-debugging-port=9222")
    # browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)


    browser=webdriver.Chrome(options=chrome_options)
    params = {
        "latitude": 50.1109,
        "longitude": 8.6821,
        "accuracy": 100
    }

    browser.execute_cdp_cmd("Page.setGeolocationOverride", params)
    # browser = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), config['DRIVER']), options=chromeOptions)
    browser.get("https://ess.emgage.work/#/login")

    # try:
    print("Step 1")
    time.sleep(2)
    print("Step 2")
    
    # company
    company = browser.find_element('xpath','/html/body/div/div/div/div[1]/div[1]/div[1]/input')
    print("Step 3")
    company.clear()
    company.send_keys(data['company'])


    buttonComp = browser.find_element('xpath','//*[@id="root"]/div/div/div[1]/div[1]/div[2]/button')
    buttonComp.click()
    print("Step 4")
    time.sleep(15)


    # username
    username = browser.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[1]/div[1]/form/div/div/input')
    username.clear()
    username.send_keys(data['user'])
    print("Step 5")

    # password
    password = browser.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[1]/div[2]/form/div/div/input')
    password.clear()
    password.send_keys(data['password'])
    print("Step 6")

    buttonLogin = browser.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[1]/div[4]/button')
    buttonLogin.click()
    print("Step 7")
    time.sleep(15)

    punchIn = browser.find_element('xpath','/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div/div/div[3]/button')
    punchIn.click()
    print("Step 8")
    time.sleep(10)

    browser.quit()
