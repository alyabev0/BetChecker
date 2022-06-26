class Team:
    def __init__(self, teamName, mapList, winRateList):
        self.teamName = teamName
        self.winRateList = winRateList
        self.mapList = mapList

    def get_age(self, mapName):
        index = mapList.index(mapName)
        return winRateList[index]

mapList = ['Dust2', 'Mirage']
winRateList = ['30%', '60%']

Navi = Team('Navi', mapList, winRateList)
print(Navi.get_age('Mirage'))