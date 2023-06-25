# 计算中奖号码的随机次数，生成随机号码
import csv
import math
import os
import threading
from datetime import datetime
from concurrent import futures

from com.sun.dushen.common import consts, utils


def run_ssq_count():
    df = utils.read_csv_data('ssq')
    thread_count = os.cpu_count() + 1
    data_split_size = math.ceil(len(df) / thread_count)

    body = []
    with futures.ThreadPoolExecutor(thread_count) as executor:
        fs = []
        for i in range(0, thread_count):
            end = data_split_size * i + data_split_size
            if end > len(df):
                end = len(df)

            f = executor.submit(sub_ssq, data_split_size * i, end, df)
            fs.append(f)

        for f in futures.as_completed(fs):
            d = f.result()[0].split(',')
            row = {
                'no': d[0],
                'date': d[1],
                'red1': d[2],
                'red2': d[3],
                'red3': d[4],
                'red4': d[5],
                'red5': d[6],
                'red6': d[7],
                'blue1': d[8],
                'count': d[9],
            }
            body.append(row)

    write_counts('ssq', ['no', 'date', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue1', 'count'], body)


def sub_ssq(start, end, df):
    print('start :: {}, end :: {}'.format(start, end))
    result = []
    for i in range(start, end):
        no = str(df.iloc[i]['no'])
        date = str(df.iloc[i]['date'])
        red1 = str(df.iloc[i]['red1'])
        red2 = str(df.iloc[i]['red2'])
        red3 = str(df.iloc[i]['red3'])
        red4 = str(df.iloc[i]['red4'])
        red5 = str(df.iloc[i]['red5'])
        red6 = str(df.iloc[i]['red6'])
        blue1 = str(df.iloc[i]['blue1'])
        bonus = [','.join([red1, red2, red3, red4, red5, red6, blue1])]
        count = ssq_count(bonus)
        result.append(','.join([no, date, red1, red2, red3, red4, red5, red6, blue1, str(count)]))
    return result


# 中奖号码的随机次数
def ssq_count(bonuses):
    for bonus in bonuses:
        i = 0
        do = True
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
            t = r + ',' + b
            if bonus == t:
                do = False

        print('thread name :: {}, time :: {}, bonus :: {}, count :: {}'.format(threading.current_thread().name,
                                                                               datetime.now().time().strftime(consts.FORMAT_TIME),
                                                                               bonus, i))
        return i


# 根据随机次数开奖
def do_ssq_bonus(i):
    while i > 0:
        i = i - 1
        r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
        b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
        t = r + ',' + b
    return t


# 进N出N
def ssq(bonuses):
    for bonus in bonuses:
        print(bonus)
        do = True
        i = 0
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
            t = r + ',' + b
            if bonus == t:
                do = False
        print(i)

        while i > 0:
            i = i - 1
            r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
            t = r + ',' + b
        print(t)


# 进N出1
def ssq2One(bonuses):
    count = 0
    t = ''
    for bonus in bonuses:
        print(bonus)
        do = True
        i = 0
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
            t = r + ',' + b
            if bonus == t:
                do = False
        print(i)
        count = count + i

    print("============================ 开奖 5,000,000 =====================================")
    j = math.ceil(count / len(bonuses))
    print(j)
    while j >= 0:
        j = j - 1
        r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
        b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
        t = r + ',' + b
    print(t)
    return t


def write_counts(file_name, file_fields, body):
    r"""create ssq data csv. """

    # name of csv file
    filename = utils.resources_path() + r'/data/{}_counts.csv'.format(file_name)

    # field names
    fields = file_fields

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        writer.writerows(body)


# 进N出N
def dlt(bonuses):
    for bonus in bonuses:
        print(bonus)
        do = True
        i = 0
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms(35, 5), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(12, 2), reverse=False))
            t = r + ',' + b
            if bonus == t:
                do = False
        print(i)

        while i > 0:
            i = i - 1
            r = ','.join(str(s) for s in sorted(utils.randoms(35, 5), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(12, 2), reverse=False))
            t = r + ',' + b
        print(t)


# 进N出1
def dlt2One(bonuses):
    count = 0
    t = ''
    for bonus in bonuses:
        print(bonus)
        do = True
        i = 0
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms(35, 5), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(12, 2), reverse=False))
            t = r + ',' + b
            if bonus == t:
                do = False
        print(i)
        count = count + i

    print("============================ 开奖 5,000,000 =====================================")
    j = math.ceil(count / len(bonuses))
    print(j)
    while j >= 0:
        j = j - 1
        r = ','.join(str(s) for s in sorted(utils.randoms(35, 5), reverse=False))
        b = ','.join(str(s) for s in sorted(utils.randoms(12, 2), reverse=False))
        t = r + ',' + b
    print(t)
    return t
