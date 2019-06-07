from selenium import webdriver

# Using FireFox to access web and need to set path to driver
driver = webdriver.Firefox("/Users/patrickutz/CS Projects/python/tableau-twitter-analytics/drivers/geckodriver")

# Open the website
driver.get("https://twitter.com")

title = driver.title()
print(title)