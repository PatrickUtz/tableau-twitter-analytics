from selenium import webdriver
import time
import keyboard
from pynput.mouse import Button, Controller
import csv
import glob
import os

mouse = Controller()

# all .csv files are downloaded to the Downloads folder now parse them into master .csv
time.sleep(3)
os.chdir("/Users/patrickutz/Downloads")
file_list = glob.glob("tweet_*")

# # clear the master file
# f = open("/Users/patrickutz/Downloads/washabstract_twitter_data.csv", "w")
# f.truncate()
# f.close()

# first_file = True
# for x in file_list:
#     reader = csv.reader(open("/Users/patrickutz/Downloads/%s" % x, 'rt'))
#     writer = csv.writer(open("/Users/patrickutz/Downloads/washabstract_twitter_data.csv", 'a'))
#     if (first_file):
#         first_file = False
#         # first_row = True
#         for row in reader:
#             writer.writerow(row)
#             # if (first_row):
#             #     first_row = False
#             # else:
#             #     writer.writerow(row)
#     else:
#         first_row = True
#         for row in reader:
#             if (first_row):
#                 first_row = False
#             else:
#                 writer.writerow(row)
    

# reader = csv.reader(open("/Users/patrickutz/Downloads/%s" % file_list[1], 'rt'))
# writer = csv.writer(open("/Users/patrickutz/Downloads/washabstract_twitter_data.csv", 'wt'))
# for row in reader:
#     writer.writerow(row)

# # delete contents of download folder
# keyboard.press_and_release('cmd+space')
# keyboard.write('terminal')
# keyboard.press_and_release('enter')
# time.sleep(2)
# keyboard.write('cd /Users/patrickutz/Downloads')
# keyboard.press_and_release('enter')
# for x in file_list:
#     keyboard.write('rm %s' % x)
#     keyboard.press_and_release('enter')


