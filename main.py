
from gettext import find
from lib2to3.pgen2 import driver
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

global browser
driver = Chrome("D:/кодинг/BetChecker/chromedriver")

driver.get("https://www.hltv.org/matches/2357189/ex-mad-lions-vs-heet-elisa-invitational-spring-2022")
sleep(3)
popup = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
popup.click()
print('popup closed')
soup = BeautifulSoup(driver.page_source, "lxml")


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

teams = soup.find_all("div", class_="teamName")
teamNames = []
teamNames.append(teams[0].text)
teamNames.append(teams[1].text)

class Team:
    def __init__(self, teamName, mapList, winRateList):
        self.teamName = teamName
        self.winRateList = winRateList
        self.mapList = mapList

    def get_mapStats(self, mapName, teamNumber):
        index = mapList.index(mapName)
        if teamNumber == 2:
            return winRateList[index*2+1]
        elif teamNumber == 1:
            return (winRateList[index*2])

Navi = Team('Navi', mapList, winRateList)
# get_mapStats показывает винрейт 1 или 2 команды на выбранной карте
print(Navi.get_mapStats('Vertigo', 2))

firstTeam = Team(teamNames[0], mapList, winRateList)
secondTeam = Team(teamNames[1], mapList, winRateList)
print(firstTeam.get_mapStats('Dust2', 1))
print(secondTeam.get_mapStats('Dust2', 2))

