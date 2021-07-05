from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import json
import time

with open("creds.json") as creds:
    c = json.load(creds)
    email = c["username"]
    password = c["password"]
    
driver = webdriver.Firefox()
# Go to your page url
driver.get('http://www.blaseball.com')
login_button = driver.find_element_by_xpath('//a[contains(@href,"/login")]')
login_button.click()
email_entry = driver.find_element_by_xpath('//input[contains(@placeholder,"Email")]')
email_entry.send_keys(email)
password_entry = driver.find_element_by_xpath('//input[contains(@placeholder,"Password")]')
password_entry.send_keys(password)
continue_button = driver.find_element_by_xpath('//input[contains(@value,"Continue")]')
continue_button.click()
# Wait for the home page to load or you'll have an error
time.sleep(5)
shop = driver.find_element_by_xpath('//a[contains(@href,"/shop")]')
shop.click()
# Didn't end up buying slots because I realized you can't buy a slot and discard it later without losing your votes
#buy_slots = driver.find_element_by_xpath('//a[contains(@href,"/pack/buy")]')
#buy_slots.click()
#submit_button = driver.find_element_by_xpath('//button[contains(@type,"submit")]')
#submit_button.click()
votes = driver.find_element_by_xpath('//button[contains(@aria-label,"Vote")]')
votes.click()
time.sleep(2)
buy_votes = driver.find_element_by_xpath('//a[contains(@href,"/buy/vote")]')
buy_votes.click()
time.sleep(2)
max_votes = driver.find_element_by_xpath('//a[contains(@class,"ModalForm-Form-Inputs-Amount-Max")]')
max_votes.click()
buy_submit_button = driver.find_element_by_xpath('//button[contains(@class,"ModalForm-Submit btn btn-success")]')
buy_submit_button.click()
driver.quit()