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
id_box.send_keys("washabstract")
pass_box.click()
pass_box.send_keys("5T4R_1)U5T")
login.click()

time.sleep(3)
time_frame = driver.find_element_by_class_name("btn.daterange-button") 
export_data = driver.find_element_by_class_name("btn.btn-default.ladda-button")
time_frame.click()  
time.sleep(2)

# TODO: Update this count whenever enter a new month cycle
total_months = 6

# download data in .csv format for each month
current_month = 3 
for x in range(total_months):
    temp_month = driver.find_element_by_xpath("/html/body/div[4]/div[4]/ul/li[%s]" % current_month)
    time.sleep(2)
    temp_month.click()
    time.sleep(2)
    export_data.click()
    time.sleep(240)
    if (current_month == 3):
        keyboard.press_and_release('down')
        keyboard.press_and_release('enter')
    else:
        keyboard.press_and_release('enter')
    print("Current month is: %s" % current_month)
    time_frame.click()  
    time.sleep(2)
    current_month += 1

# all .csv files are downloaded to the /Downloads folder now parse them into the master .csv
time.sleep(3)
os.chdir("/Users/patrickutz/Downloads")
file_list = glob.glob("tweet_*")

# clear the master file
f = open("/Users/patrickutz/Downloads/washabstract_twitter_data.csv", "w")
f.truncate()
f.close()

first_file = True
for x in file_list:
    reader = csv.reader(open("/Users/patrickutz/Downloads/%s" % x, 'rt'))
    writer = csv.writer(open("/Users/patrickutz/Downloads/washabstract_twitter_data.csv", 'a'))
    if (first_file):
        first_file = False
        for row in reader:
            writer.writerow(row)
    else:
        first_row = True
        for row in reader:
            if (first_row):
                first_row = False
            else:
                writer.writerow(row)

time.sleep(3)

# delete contents of /Downloads folder
keyboard.press_and_release('cmd+space')
keyboard.write('terminal')
keyboard.press_and_release('enter')
time.sleep(2)
keyboard.write('cd /Users/patrickutz/Downloads')
keyboard.press_and_release('enter')
for x in file_list:
    keyboard.write('rm %s' % x)
    keyboard.press_and_release('enter')

# update data on Tableau
keyboard.press_and_release('cmd+space')
keyboard.write('tab')
keyboard.press_and_release('enter')
time.sleep(4)
mouse.position = (190, 11)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(4)
mouse.position = (190, 95)
time.sleep(4)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(4)
keyboard.press_and_release("enter")
time.sleep(4)
keyboard.press_and_release("enter")
time.sleep(6)

# upload data to Tableau Public
mouse.position = (656, 8)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(4)
mouse.position = (656, 178)
time.sleep(4)
mouse.position = (1013, 196)
mouse.press(Button.left)
mouse.release(Button.left)
