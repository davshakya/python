from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import requests

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")


# provide website url here
# driver.get("http://demo.guru99.com/test/newtours/")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


# get all links
all_links = driver.find_elements(By.TAG_NAME, "a")

# check each link if it is broken or not
for link in all_links:
    # extract url from href attribute
    url = link.get_attribute('href')

    # send request to the url and get the result
    result = requests.head(url)

    # if status code is not 200 then print the url (customize the if condition according to the need)
    if result.status_code != 200:
        print(url, result.status_code)
