# 数据爬取

import csv

import requests
from bs4 import BeautifulSoup

from com.sun.dushen.common import utils

url = 'http://datachart.500.com/dlt/history/newinc/history.php?start=03001&end=99999&sort=1'


def run():
    data = agent()
    write(data)


def agent():
    r"""agent dlt data. """

    r = requests.get(url)
    html = BeautifulSoup(r.text, 'lxml')
    tr = html.select("#tdata tr")

    result = []
    for item in tr:

        # red = utils.randoms(35, 5)
        # blue = utils.randoms(12, 2)

        td = item.contents
        data = {
            # 期号
            'no': td[1].text,
            # 开奖日期
            'date': td[15].text.replace("-", ''),
            # 红球号码(5)[1-35]
            'red1': td[2].text,
            'red2': td[3].text,
            'red3': td[4].text,
            'red4': td[5].text,
            'red5': td[6].text,
            # 蓝球号码(2)[1-12]
            'blue1': td[7].text,
            'blue2': td[8].text,
            # 红球号码(5)[1-35]
            # 'dummy_red1': red[0],
            # 'dummy_red2': red[1],
            # 'dummy_red3': red[2],
            # 'dummy_red4': red[3],
            # 'dummy_red5': red[4],
            # 'dummy_red6': 6,
            # 'dummy_red7': 7,
            # 'dummy_red8': 8,
            # 'dummy_red9': 9,
            # 'dummy_red10': 10,
            # 'dummy_red11': 11,
            # 'dummy_red12': 12,
            # 'dummy_red13': 13,
            # 'dummy_red14': 14,
            # 'dummy_red15': 15,
            # 'dummy_red16': 16,
            # 'dummy_red17': 17,
            # 'dummy_red18': 18,
            # 'dummy_red19': 19,
            # 'dummy_red20': 20,
            # 'dummy_red21': 21,
            # 'dummy_red22': 22,
            # 'dummy_red23': 23,
            # 'dummy_red24': 24,
            # 'dummy_red25': 25,
            # 'dummy_red26': 26,
            # 'dummy_red27': 27,
            # 'dummy_red28': 28,
            # 'dummy_red29': 29,
            # 'dummy_red30': 30,
            # 'dummy_red31': 31,
            # 'dummy_red32': 32,
            # 'dummy_red33': 33,
            # 'dummy_red34': 34,
            # 'dummy_red35': 35,
            # 蓝球号码(2)[1-12]
            # 'dummy_blue1': blue[0],
            # 'dummy_blue2': blue[1],
            # 'dummy_blue3': 3,
            # 'dummy_blue4': 4,
            # 'dummy_blue5': 5,
            # 'dummy_blue6': 6,
            # 'dummy_blue7': 7,
            # 'dummy_blue8': 8,
            # 'dummy_blue9': 9,
            # 'dummy_blue10': 10,
            # 'dummy_blue11': 11,
            # 'dummy_blue12': 12,
        }
        result.append(data)

    # print("dlt", result)
    return result


def write(body):
    r"""create dlt data csv. """

    # name of csv file
    filename = utils.resources_path() + r'/data/dlt.csv'

    # field names
    fields = ['no', 'date', 'red1', 'red2', 'red3', 'red4', 'red5', 'blue1', 'blue2',
              # 'dummy_red1', 'dummy_red2', 'dummy_red3', 'dummy_red4', 'dummy_red5', #'dummy_red6', 'dummy_red7', 'dummy_red8', 'dummy_red9', 'dummy_red10',
              # 'dummy_red11', 'dummy_red12', 'dummy_red13', 'dummy_red14', 'dummy_red15', 'dummy_red16', 'dummy_red17', 'dummy_red18', 'dummy_red19', 'dummy_red20',
              # 'dummy_red21', 'dummy_red22', 'dummy_red23', 'dummy_red24', 'dummy_red25', 'dummy_red26', 'dummy_red27', 'dummy_red28', 'dummy_red29', 'dummy_red30',
              # 'dummy_red31', 'dummy_red32', 'dummy_red33', 'dummy_red34', 'dummy_red35',
              # 'dummy_blue1', 'dummy_blue2', #'dummy_blue3', 'dummy_blue4', 'dummy_blue5', 'dummy_blue6', 'dummy_blue7', 'dummy_blue8', 'dummy_blue9', 'dummy_blue10',
              # 'dummy_blue11', 'dummy_blue12'
              ]

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        writer.writerows(body)
