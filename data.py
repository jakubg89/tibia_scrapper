# check worlds, skills
import requests
from bs4 import BeautifulSoup
from get_proxy import get_one_proxy, headers

# professions
# 1 : None
# 2 : Knights
# 3 : Paladins
# 4 : Sorcerers
# 5 : Druids

# category - can be picked any to scrap whole highscores of selected category
# 1 : Achievements
# 2 : Axe Fighting
# 15 : Boss Points
# 3 : Charm Points
# 4 : Club Fighting
# 5 : Distance Fighting
# 14 : Drome Score
# 6 : Experience Points
# 7 : Fishing
# 8 : Fist Fighting
# 9 : Goshnar's Taint
# 10 : Loyalty Points
# 11 : Magic Level
# 12 : Shielding
# 13 : Sword Fighting


def world():
    worlds = []
    url = 'https://www.tibia.com/community/?subtopic=highscores'
    request_headers = headers()
    proxy = {
        "http": get_one_proxy(),
    }
    soup = BeautifulSoup(requests.get(url, headers=request_headers, proxies=proxy).text, 'html.parser')
    for option in soup.find_all('select', {'name': 'world'}):
        for i in option.findAll('option'):
            if i['value'] != '':
                worlds.append(i['value'])
    return worlds


def profession():
    prof = [2, 3, 4, 5]
    return prof


def category():
    # skill = [1, 2, 15, 3, 4, 5, 14, 6, 7, 8, 9, 10, 11, 12, 13]
    skill = 6
    return skill

