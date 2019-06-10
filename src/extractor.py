from selenium import webdriver
import time
import keyboard
from pynput.mouse import Button, Controller
import csv
import glob
import os

mouse = Controller()

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

# TODO: increase this time to like a minute because it takes a while for the .csv file to be ready
# wait for export data to be prepared to download
time.sleep(20)
keyboard.press_and_release('down')
keyboard.press_and_release('enter')

time.sleep(3)
os.chdir("/Users/patrickutz/Downloads")
file_list = glob.glob("tweet_*")

reader = csv.reader(open("/Users/patrickutz/Downloads/%s" % file_list[0], 'rt'))
writer = csv.writer(open("/Users/patrickutz/Downloads/washabstract_twitter_data.csv", 'wt'))
for row in reader:
    writer.writerow(row)

time.sleep(3)
# delete contents of download folder
keyboard.press_and_release('cmd+space')
keyboard.write('terminal')
keyboard.press_and_release('enter')
time.sleep(2)
keyboard.write('cd /Users/patrickutz/Downloads')
keyboard.press_and_release('enter')
keyboard.write('rm %s'%file_list[0])
keyboard.press_and_release('enter')

# update data on Tableau
keyboard.press_and_release('cmd+space')
keyboard.write('tab')
keyboard.press_and_release('enter')
time.sleep(2)
keyboard.press_and_release('cmd+r')
time.sleep(1)

# Set pointer position
mouse.position = (656, 8)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(2)
mouse.position = (656, 178)
time.sleep(2)
mouse.position = (1013, 196)
mouse.press(Button.left)
mouse.release(Button.left)
