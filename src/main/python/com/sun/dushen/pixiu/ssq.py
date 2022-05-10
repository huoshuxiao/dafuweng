import csv

import requests
from bs4 import BeautifulSoup

url = 'http://datachart.500.com/ssq/history/newinc/history.php?start=03001&end=99999&sort=1'


def run():
    data = agent()
    writeCsv(data)


def agent():
    r"""ssq."""

    r = requests.get(url)
    html = BeautifulSoup(r.text, 'lxml')
    tr = html.select("#tdata tr")

    result = []
    # result = list()
    for item in tr:
        td = item.contents
        # data = dict()
        data = {
            # 期号
            'no': td[1].text,
            # 开奖日期
            'date': td[16].text,
            # 红球号码(6)[1-33]
            'red1': td[2].text,
            'red2': td[3].text,
            'red3': td[4].text,
            'red4': td[5].text,
            'red5': td[6].text,
            'red6': td[7].text,
            # 蓝球号码(1)[1-16]
            'blue1': td[8].text,
            # 红球号码[1-33]
            'dummy_red1': 1,
            'dummy_red2': 2,
            'dummy_red3': 3,
            'dummy_red4': 4,
            'dummy_red5': 5,
            'dummy_red6': 6,
            'dummy_red7': 7,
            'dummy_red8': 8,
            'dummy_red9': 9,
            'dummy_red10': 10,
            'dummy_red11': 11,
            'dummy_red12': 12,
            'dummy_red13': 13,
            'dummy_red14': 14,
            'dummy_red15': 15,
            'dummy_red16': 16,
            'dummy_red17': 17,
            'dummy_red18': 18,
            'dummy_red19': 19,
            'dummy_red20': 20,
            'dummy_red21': 21,
            'dummy_red22': 22,
            'dummy_red23': 23,
            'dummy_red24': 24,
            'dummy_red25': 25,
            'dummy_red26': 26,
            'dummy_red27': 27,
            'dummy_red28': 28,
            'dummy_red29': 29,
            'dummy_red30': 30,
            'dummy_red31': 31,
            'dummy_red32': 32,
            'dummy_red33': 33,
            # 蓝球号码[1-16]
            'dummy_blue1': 1,
            'dummy_blue2': 2,
            'dummy_blue3': 3,
            'dummy_blue4': 4,
            'dummy_blue5': 5,
            'dummy_blue6': 6,
            'dummy_blue7': 7,
            'dummy_blue8': 8,
            'dummy_blue9': 9,
            'dummy_blue10': 10,
            'dummy_blue11': 11,
            'dummy_blue12': 12,
            'dummy_blue13': 13,
            'dummy_blue14': 14,
            'dummy_blue15': 15,
            'dummy_blue16': 16,
        }
        result.append(data)

    return result


def writeCsv(body):

    # name of csv file
    filename = "../.././../dlt.csv"

    # field names
    fields = ['no', 'date', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue1',
              'dummy_red1', 'dummy_red2', 'dummy_red3', 'dummy_red4', 'dummy_red5', 'dummy_red6', 'dummy_red7', 'dummy_red8', 'dummy_red9', 'dummy_red10',
              'dummy_red11', 'dummy_red12', 'dummy_red13', 'dummy_red14', 'dummy_red15', 'dummy_red16', 'dummy_red17', 'dummy_red18', 'dummy_red19', 'dummy_red20',
              'dummy_red21', 'dummy_red22', 'dummy_red23', 'dummy_red24', 'dummy_red25', 'dummy_red26', 'dummy_red27', 'dummy_red28', 'dummy_red29', 'dummy_red30',
              'dummy_red31', 'dummy_red32', 'dummy_red33',
              'dummy_blue1', 'dummy_blue2', 'dummy_blue3', 'dummy_blue4', 'dummy_blue5', 'dummy_blue6', 'dummy_blue7', 'dummy_blue8', 'dummy_blue9', 'dummy_blue10',
              'dummy_blue11', 'dummy_blue12', 'dummy_blue13', 'dummy_blue14', 'dummy_blue15', 'dummy_blue16']

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        writer.writerows(body)
