# create proxy list
import requests
from bs4 import BeautifulSoup
import pandas as pd


def headers():
    headers_list = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                  ' Chrome/99.0.4844.74 Safari/537.36'}
    return headers_list


def scrap_proxy():
    url = 'https://free-proxy-list.net/'
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    tables = soup.find('table', {'class': 'table table-striped table-bordered'})
    data = pd.DataFrame(columns=['ip',
                                 'port',
                                 'code',
                                 'country',
                                 'anonymity',
                                 'google',
                                 'https',
                                 'last checked'])

    for row in tables.findAll('tr'):
        columns = row.find_all('td')
        if columns != []:
            ip = columns[0].text.strip()
            port = columns[1].text.strip()
            code = columns[2].text.strip()
            country = columns[3].text.strip()
            anonymity = columns[4].text.strip()
            google = columns[5].text.strip()
            https = columns[6].text.strip()
            last_checked = columns[7].text.strip()

            data2 = {'ip': ip,
                     'port': port,
                     'code': code,
                     'country': country,
                     'anonymity': anonymity,
                     'google': google,
                     'https': https,
                     'last checked': last_checked}
            data3 = pd.DataFrame(data=data2, index=[0])

            data = pd.concat([data, data3], ignore_index=True)


def proxy_list():
    temp_list = [
        '139.162.182.54:49165',
        '96.126.124.197:81',
        '80.48.119.28:8080',
        '198.59.191.234:8080',
        '71.86.129.131:8080',
        '185.125.125.157:80'
    ]
    return temp_list


def get_one_proxy():
    pass
