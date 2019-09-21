import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

import sys
import requests
from bs4 import BeautifulSoup

from django.core.files import File
from lotto.models import Winnum


def trim(s):
    return ' '.join(s.split())

def main(r):
    for r in range(1, r+1):
        url = 'https://m.dhlottery.co.kr/gameResult.do'
        params = {'method': 'byWin', 'drwNo': r}
        response = requests.get(url, params=params)
        html = response.text
        print(f"{r}회차 접속")
        soup = BeautifulSoup(html, 'html.parser')

        list=[]
        for i_int in soup.select('.bx_lotto_winnum .ball'):
            num = int(i_int.text)
            list.append(num)
        print(list)

        winneramount = soup.findAll("td")[0].text.replace("개", "명")
        perprize = soup.findAll("td")[3].text
        winmethod = soup.findAll("td")[4].text
        winnum = Winnum(round=r, num1=list[0], num2=list[1], num3=list[2], num4=list[3], num5=list[4], num6=list[5], bounusnum=list[6], winneramount=winneramount, perprize=perprize, winmethod=winmethod)
        winnum.save()

        print(winnum)


if __name__ == '__main__':
    # try :
    #     query = sys.argv[1]
    #     main(query)
    # except IndexError:
    #     print(f'usage> {sys.argv[0]} <query>')
    main(876)