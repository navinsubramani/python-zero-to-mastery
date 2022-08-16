# Install the Selenium
# Install the WebDrivers based on the browser
# for Chrome Browser: https://sites.google.com/chromium.org/driver/

from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

CHROMEDRIVE_EXE_PATH = os.path.dirname(__file__) + '/chromedriver.exe'
chrome_browser = webdriver.Chrome(CHROMEDRIVE_EXE_PATH)
chrome_browser.implicitly_wait(10)

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')


# Validate and print if the web title name is correct
print(chrome_browser.title == 'Selenium Easy Demo - Simple Form to Automate using Selenium')


# Get the button text from the website
# Because there is a ad popup , we need to close the ad first
close_button = chrome_browser.find_element('class name', 'at4-close')
print("****----Ad popup found----****")
print(close_button.get_attribute('innerHTML'))
close_button.click()
print("****----Ad popup closed----****")

# works with the actual page
print("****----Start of 'Single Input Field' Test----****")
inp = "I am cool...."
inp_field = chrome_browser.find_elements('id', 'user-message')[0]
inp_field.clear()
inp_field.send_keys(inp)

button = chrome_browser.find_element('class name','btn.btn-default')
button.click()

out = chrome_browser.find_element('id','display').get_attribute('innerHTML')
print("PASS") if inp == out else print(f"FAILED because input = {inp} and ouput = {out}")
print("****----End of 'Single Input Field' Test----****")

# close the browser
chrome_browser.close()