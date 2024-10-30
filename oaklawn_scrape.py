#importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium_move_cursor.MouseActions import move_to_element_chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#import js
#import json
import numpy as np
import time
#import pandas as pd         #to save CSV file
from bs4 import BeautifulSoup
#import ctypes         #to create text popup

#defining browser and adding the “ — headless” argument
opts = Options()
opts.add_argument(' — headless')
driver = webdriver.Chrome(options=opts)
url = 'https://oaklawnsports.com/sports.shtml#home'
driver.maximize_window() #maximize the window
driver.get(url)          #open the URL
driver.implicitly_wait(220) #maximum time to load the link
driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")
#//*[@id="KambiBC-core-ux-landing-page"]/div[3]/div/div/div[1]/div[1]/div/div/div/ul/li[3]/div
#//*[@id="KambiBC-core-ux-landing-page"]/div[3]/div/div/div[1]/div[1]/div/div/div/ul/li[3]/div
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="KambiBC-core-ux-landing-page"]/div[3]/div/div/div[1]/div[1]/div/div/div/ul/li[2]/div')
time.sleep(5)
element.click()
time.sleep(2)
driver.implicitly_wait(220)

#extract the number of pages for the searched product
driver.implicitly_wait(120)
time.sleep(3)

open_wagers_ele = driver.find_element(By.XPATH, '//*[@id="KambiBC-core-ux-landing-page"]/div[3]/div/div/section/section/section/ul/li[2]/div/a/div/div')
time.sleep(5)
open_wagers_ele.click()
time.sleep(2)
list_headers = driver.find_elements(By.XPATH, '//li[@class="KambiBC-bet-offer-category"]')
print(f'{list_headers}')
for element in list_headers:
    element.click()
    time.sleep(1)

result = driver.page_source
soup = BeautifulSoup(result, 'html.parser')
page = list(soup.findAll('div', class_="KambiBC-bet-offer-subcategory__container"))
for item in page:
    print(f"{item.text}")