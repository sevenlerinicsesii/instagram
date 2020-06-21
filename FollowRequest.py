#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################################################
# File name: FollowRequests.py                           #
# Author = BEKTES FURKAN                                 #
# Mail : 'bektes.fukan.pro@gmail.com'                    #
# Author's instagram : @jesuisfurkan                     #
##########################################################

import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

username = 'Nervensystem' # without @ 
password = 'Beratberk6082'

# Function that approve each follow request
def Approve():
    print("Follow Requests are approving")
    i = 0 # Number of approved follow
    incr = 0 # increment
    if driver.find_elements_by_xpath("//button[contains(.,'Approve')]"):
        elements = driver.find_elements_by_xpath("//button[contains(.,'Approve')]")
        try:
            for btn in elements:
                btn.click()
                i += 1
                if i == incr:
                    print("Number of approved follow:", i)
                    incr += 10
                time.sleep(3) # 3 seconds (for each request) is recommended else you can be banned
            print("Number of approved follow:", i)
            Approve()
        except:
            driver.refresh()
            time.sleep(4)
            Approve()
    else:
        print("Each follow request are approved. Sleep 2 minutes ...")
        time.sleep(120)
        driver.refresh()
        print("Driver refresh")
        time.sleep(4)
        Approve()


options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Common Files\Oracle\Java\javapath', chrome_options=options) # like '/Users/xxxx/Desktop/chromedriver'

getDriver = ("https://www.instagram.com/accounts/activity?followRequests=")
try:
    driver.get(getDriver)
    time.sleep(4)
    # Select English Language
    driver.find_element_by_class_name('hztqj').click()
    Select(driver.find_element_by_class_name('hztqj')).select_by_value('en')
    time.sleep(4)
    # Input username & password
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    print("Connection Established to your instagram")
    time.sleep(5)
    Approve()
except:
    print("Connection NOT Established. Please check your network")
