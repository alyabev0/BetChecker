
from lib2to3.pgen2 import driver
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

global browser
driver = Chrome("D:/кодинг/BetChecker/chromedriver")
driver.get("https://www.hltv.org/matches/2356961/honoris-vs-into-the-breach-esport-tour-2022-series-2")
# element = browser.find_element(By.CLASS_NAME, "mw-headline")
# print("element=", element)
time.sleep(3)
popup = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
popup.click()
print('success')
soup = BeautifulSoup(driver.page_source, "lxml")
elements = soup.find_all("div", class_="map-stats-infobox")
for element in elements:
   print(element.text)