import requests
import random
from bs4 import BeautifulSoup
from time import sleep
import data
import get_proxy


class ScrapHighscores:
    def __init__(self):
        category = data.category()
        self.request_headers = get_proxy.headers()
        self.proxy_list = get_proxy.proxy_list()

        self.how_many_sites = 0
        self.path = 'temp/0910 list.csv'
        self.column_count = 1
        self.block_first_row = 1
        self.text = ''

        self.access = True
        self.access2 = True
        self.proxy_num = 0

        for world in data.world():
            print(world, ' ', end='')
            sleep(round(random.randint(5, 20)))
            for prof in data.profession():
                self.url = 'https://www.tibia.com/community/?subtopic=highscores&' \
                            'world={world}&' \
                            'beprotection=-1&' \
                            'category={category}&' \
                            'profession={prof}&' \
                            'currentpage=1'.format(world=world,
                                                   prof=prof,
                                                   category=category)
                print(prof, end='')
                self.check = self.count_sites() + 1
                for site_num in range(1, self.check):
                    self.url2 = 'https://www.tibia.com/community/?subtopic=highscores&' \
                                'world={world}&' \
                                'beprotection=-1&' \
                                'category={category}&' \
                                'profession={prof}&' \
                                'currentpage={cur_page}'.format(world=world,
                                                                prof=prof,
                                                                cur_page=site_num,
                                                                category=category)

                    self.access2 = True
                    while self.access2:
                        self.proxies = {
                            "http": self.proxy_list[self.proxy_num],
                        }
                        self.soup = BeautifulSoup(requests.get(self.url2,
                                                               headers=self.request_headers,
                                                               proxies=self.proxies).text, 'html.parser')

                        # zmienić na sprawdzenie statusu lub wyrzucic do funkcji
                        self.xyz = self.soup.findAll('title')[0].text
                        if self.xyz == '403 Forbidden':
                            self.access2 = True
                            sleep(round(random.uniform(0.1, 0.2), 3))
                            self.proxy_num += 1
                            if self.proxy_num == len(self.proxy_list):
                                self.proxy_num = 0
                        else:
                            self.scrap_sub_site()
                            sleep(round(random.uniform(0.1, 0.2), 3))
                            print(str(site_num) + '/' + str(self.check) + '-', end='')
                            print('ok ', end='')
                            # każde zapytanie z innego proxy z listy - w teorii
                            self.proxy_num += 1
                            if self.proxy_num >= len(self.proxy_list):
                                self.proxy_num = 0
                            print(self.proxy_list[self.proxy_num], self.proxy_num, len(self.proxy_list))
                            self.access2 = False
                print()
                self.check = 0

    def count_sites(self):
        self.how_many_sites = 0
        self.access = True
        while self.access:
            self.proxies = {
                "http": self.proxy_list[self.proxy_num],
            }
            self.soup = BeautifulSoup(requests.get(self.url,
                                                   headers=self.request_headers,
                                                   proxies=self.proxies).text, 'html.parser')

            # zmienic na sprawdzenie statusu "odpowiedz.status_code
            self.xyz = self.soup.findAll('title')[0].text
            if self.xyz == '403 Forbidden':
                self.access = True
                sleep(round(random.uniform(0.25, 0.4), 3))
                self.proxy_num += 1
                print(self.proxy_num, end='')
                if self.proxy_num > len(self.proxy_list):
                    self.proxy_num = 0
            else:
                print('ok')
                self.access = False
                for self.i in self.soup.findAll('span', {'class': 'PageLink'}):
                    self.how_many_sites += 1
                self.how_many_sites = int(self.how_many_sites / 2)
                return self.how_many_sites
        return self.how_many_sites

    def scrap_sub_site(self):
        for div in self.soup.findAll('div', {'class': 'TableContentContainer'}):
            self.text = ''
            self.block_first_row = 1
            for i in div.findAll('td'):
                # pierwsza pozycja jeżeli jest Auto Incracment
                if self.column_count == 1:
                    self.text = 'NULL'

                # koniec wiersza, wpisanie calego ciagu do pliku w celu bulk
                elif self.column_count == 6:
                    self.column_count = 0
                    self.text = self.text + ',"'
                    self.text = self.text + i.text.replace(',', '') + '"'
                    self.text = self.text + '\n'

                    if self.block_first_row != 1:
                        self.savefile(self.text)
                    self.block_first_row += 1
                else:
                    self.text = self.text + ',"'
                    self.text = self.text + i.text + '"'
                self.column_count += 1

    def savefile(self, text):
        with open(self.path, 'a') as self.file:
            self.file.write(text)
        self.file.close()


ScrapHighscores()
