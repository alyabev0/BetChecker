
from gettext import find
from lib2to3.pgen2 import driver
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

global browser
driver = Chrome("D:/кодинг/BetChecker/chromedriver")

driver.get("https://www.hltv.org/matches/2357056/masonic-vs-flet-esea-advanced-season-41-europe")
time.sleep(3)
popup = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
popup.click()
print('popup closed')
soup = BeautifulSoup(driver.page_source, "lxml")
statElements = soup.find_all("div", class_="map-stats-infobox")
mapsInfo = soup.find_all("div", class_="map-stats-infobox-maps")

winRateList = []
mapList = []
for mapInfo in mapsInfo:
    mapName = mapInfo.find('img').attrs['alt']
    mapList.append(mapName)
    mapStats = mapInfo.find_all('a', class_='a-reset')
    for mapStat in mapStats:
        mapStat = mapStat.text
        winRateList.append(mapStat)
    print(mapList, winRateList)
else: 
    print('end of array')


class Team:
    def __init__(self, teamName, mapList, winRateList):
        self.teamName = teamName
        self.winRateList = winRateList
        self.mapList = mapList

    def get_age(self, mapName, teamNumber):
        index = mapList.index(mapName)
        if teamNumber == 2:
            return winRateList[index*2+1]
        elif teamNumber == 1:
            print((index*2))
            return (winRateList[index*2])

Navi = Team('Navi', mapList, winRateList)
print(Navi.get_age('Vertigo', 1))