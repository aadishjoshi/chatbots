'''
***************************************************************************************************
Written by: Aadish Joshi
email: aadish.joshi@utdallas.edu
Date: April 20, 2019

Written for educational use only.

To run:
 - pip install selenium
 - Download chrome driver using: https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_win32.zip
 - run this file
***************************************************************************************************
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.jobscan.co/')

element = driver.find_elements_by_id("trySampleCta")
for e in element:
    e.click()

try:
    nullelement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "matchRate"))
    )
    buttons = driver.find_elements_by_xpath("//*[contains(text(), 'End tour')]")
    for e in buttons:
        e.click()

    rescan = driver.find_elements_by_id("btn-re-scan")
    rescan[0].click()
    
except:
    driver.quit()    

