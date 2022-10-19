# create proxy list
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random


def headers():
    headers_list = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                  ' Chrome/99.0.4844.74 Safari/537.36'}
    return headers_list


def scrap_proxy():
    url = 'https://free-proxy-list.net/'
    request = requests.get(url)
    proxy_tables = pd.read_html(request.text)
    proxy_table = pd.DataFrame(data=proxy_tables[0])
    proxy_table = proxy_table[proxy_table['Anonymity'] == 'elite proxy']
    proxy_table = proxy_table[['IP Address', 'Port']].reset_index(drop=True).drop_duplicates(subset='IP Address')
    proxy_table.to_csv('proxy_list.csv', header=False,  index=False, sep=':', mode='w')


def proxy_list():
    temp_list = []
    with open('proxy_list.csv') as file:
        for line in file:
            line = line.strip()
            temp_list.append(line)
    # temp_list = [x for x in temp_list if x]
    temp_list.pop()
    return temp_list


def get_one_proxy():
    proxy = proxy_list()
    random.shuffle(proxy)
    proxy = proxy[0]
    return proxy


scrap_proxy()
x = proxy_list()
for i in x:
    print(i)
print(get_one_proxy())

print('hello worlds')
