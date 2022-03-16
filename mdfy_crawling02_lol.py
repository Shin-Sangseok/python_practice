from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

name_list=[]
rank_list=[]
level_list=[]
win_list=[]

for i in range(1, 11):
    con=request.urlopen('https://www.op.gg/leaderboards/tier?page='+str(i)+'&region=kr')
    doc = BeautifulSoup(con, 'html.parser')
    if i==1:
        name_list+=doc.select('.name')
    name_list+=doc.select('strong')
    name_list.pop()
    rank_list+=doc.select('.rank')
    level_list+=doc.select('.level')
    win_list+=doc.select('.w')
# op.gg 사이트의 1~10페이지까지 플레이어 랭킹 정보를 크롤링하여 list에 저장

len(name_list), len(rank_list), len(level_list), len(win_list) #데이터의 row는 1000개

name_text = []
for one in name_list:
    name_text.append(one.text)

rank_text = []
for one in rank_list:
    rank_text.append(one.text)

level_text = []
for one in level_list:
    level_text.append(one.text)

win_text = []
for one in win_list:
    win_text.append(one.text)
# 크롤링한 데이터의 text만 추출하여 list에 저장

for i in range(1, 5):
    temp = level_text[i].split('.')
    level_text[i] = temp[1]
# 랭킹 2~5위 유저의 레벨은 Lv. 접두어가 포함되므로, 이를 통일시키기 위해 Lv.을 제거하고 넣어주는 전처리가 필요

lol_player_file=open('lol_player.csv', 'w', encoding = 'utf8')
lol_player_file.write('rank,name,level,win\n')

for i in range(1000):
    lol_player_file.write(rank_text[i] + ',' +
                         name_text[i] + ',' +
                         level_text[i]+ ',' +
                         win_text[i] + '\n')
    
lol_player_file=open('lol_player.csv', 'a', encoding = 'utf8')
player= pd.read_csv('lol_player.csv')
player
