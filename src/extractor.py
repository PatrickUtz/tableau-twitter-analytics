from selenium import webdriver
import time
import keyboard

# Using FireFox to access web and need to set path to driver
driver = webdriver.Firefox(executable_path="/Users/patrickutz/cs-projects/python/tableau-twitter-analytics/drivers/geckodriver")

# Open the website
driver.get("https://analytics.twitter.com/user/WashAbstract/tweets") 

id_box = driver.find_element_by_class_name("js-username-field.email-input.js-initial-focus")
pass_box = driver.find_element_by_class_name("js-password-field")
login = driver.find_element_by_class_name("submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")

# wait for page to load
time.sleep(4)

# send id and password info
id_box.click()
id_box.send_keys("")
pass_box.click()
pass_box.send_keys("")
login.click()

time.sleep(3)
export_data = driver.find_element_by_class_name("btn.btn-default.ladda-button")
export_data.click()

# wait for export data to be prepared to download
time.sleep(10)
keyboard.press_and_release('enter')
