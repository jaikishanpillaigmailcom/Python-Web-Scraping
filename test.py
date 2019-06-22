import selenium
import csv
from selenium import webdriver
import time

with open("abc.csv") as f1:
	csvrow=csv.reader(f1,delimiter=",")
	for row in csvrow:
		email=row[0]
		pswd=row[1]

options=webdriver.ChromeOptions()
options.add_argument("--diable-notification")
driver=webdriver.Chrome("C:/Users/admin/Downloads/chromedriver_win32/chromedriver.exe",options=options)
driver.maximize_window()
time.sleep(10)

driver.get("https://www.linkedin.com/login")

driver.find_element_by_id("username").send_keys(email)
driver.find_element_by_id("password").send_keys(pswd)
driver.find_element_by_xpath('//button[text()="Sign in"]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="ember33"]/input').send_keys("sap consultant")
driver.find_element_by_xpath('//*[@id="nav-search-controls-wormhole"]/button').click()
time.sleep(10)
driver.find_element_by_css_selector('button.search-vertical-filter__filter-item-button').click()
time.sleep(5)
driver.find_element_by_css_selector('span.name.actor-name').click()
