from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

con = request.urlopen('https://www.op.gg/leaderboards/tier?region=kr')
con

con.status

doc = BeautifulSoup(con, 'html.parser')
doc

name_list = []
excellent = doc.select('#iiwandy > a')
name_list.append(excellent[0].text)

name_list

second = doc.select(' a > span[class="name"]')
for order in second:
    name_list.append(order.text)
name_list

number_first = doc.select('strong') #6위부터 아래 순위까지
number_first[0].text


for order in number_first:
    name_list.append(order.text)
name_list
#len(people_name)-1
name_list.remove('Privacy Policy')
len(name_list)

ranking_list = []
ranking_excel = doc.select('div.rank')
for order in ranking_excel:
    ranking_list.append(order.text)
ranking_list

ranking_below = doc.select('td.rank')
for order in ranking_below:
    ranking_list.append(order.text)
ranking_list
len(ranking_list)

level_list = []
level_first = doc.select('div.icon > a > div')
level_list.append(level_first[0].text)

level_second = doc.select('div.tier-rank > div')
level_second
for order in range(0,4):
    level1 = level_second[order].text.split('.')
    #print(level1[1])
    level_list.append(level1[1])
   # level_list.append(order.text)
level_list

level_other = doc.select('td.level')
level_other
for other in level_other:
    level_list.append(other.text)
level_list
len(level_list)

win_list = []
win_first = doc.select('div.w')
for order in win_first:
    win_list.append(order.text)
win_list
len(win_list)

for i in range(2, 11):
    con = request.urlopen('https://www.op.gg/leaderboards/tier?page=' + str(i) + '&region=kr')
    doc = BeautifulSoup(con, 'html.parser')

    # name_list
    plus_name = doc.select('strong')
    for order in plus_name:
        name_list.append(order.text)

    # ranking_list
    plus_rank = doc.select('.rank')
    for order in plus_rank:
        ranking_list.append(order.text)

    # level_list
    plus_level = doc.select('.level')
    for order in plus_level:
        level_list.append(order.text)

    # win_list
    plus_win = doc.select('.w')
    for order in plus_win:
        win_list.append(order.text)

    for i in range(1, 10):
        try:
            name_list.remove('Privacy Policy')
        except ValueError:
            pass

len(name_list)
len(ranking_list)
len(level_list)
len(win_list)

lol_player_file = open('lol_player.csv','w',encoding='utf8')
lol_player_file.write('rank,name,level,win'+'\n')

for i in range(1000):
    lol_player_file.write(ranking_list[i]+','+
                          name_list[i]+','+
                          level_list[i]+','+
                          win_list[i]+'\n')

lol_player_file.close()

player = pd.read_csv('lol_player.csv')
player