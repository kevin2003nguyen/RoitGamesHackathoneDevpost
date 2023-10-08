from collections import OrderedDict

team = {
    "JDG": ["LPL",1,1,1],
    "BLG": ["LPL",2,3,2],
    "LNG": ["LPL",5,2,0],
    "WBG": ["LPL",5,5,0],
    "GENG": ["LCK",1,1,4],
    "T1": ["LCK",2,2,3],
    "KT": ["LCK",3,3,0],
    "DPLUS": ["LCK",5,4,0],
    "NRG": ["LCS",6,1,0],
    "TL": ["LCS",8,3,0],
    "C9": ["LCS",1,2,5],
    "G2": ["LEC",4,1,7],
    "FNC": ["LEC",8,3,0],
    "MAD": ["LEC", 1,7,0]


}

region = 0
regionMultiplier = {
    "LPL" : 3,
    "LCK" : 2.9,
    "LEC" : 1.3,
    "LCS" : 1

}
spring = 1
summer = 2
msi = 3

ranking = {}

for t in team:
    springPoint = (320/team[t][spring])*0.75
    msiPoint = msiPoint = (320 / team[t][msi]) * 0.15 if team[t][msi] != 0 else 0
    summerPoint = (320/team[t][summer])
    regionName = team[t][region]
    if(team[t][msi]!=0):
        ranking[t] = (springPoint + msiPoint + summerPoint) * regionMultiplier[regionName]
    else:
        ranking[t] = (springPoint + summerPoint) * regionMultiplier[regionName]
    
sorted_ordered_dict = OrderedDict(sorted(ranking.items(), key=lambda item: item[1]))
finalRanking = list(sorted_ordered_dict.keys())[::-1]
print(finalRanking)
        
