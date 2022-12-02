import datetime

from com.sun.dushen.common import utils
from com.sun.dushen.model.lottery import probability, l_model
from com.sun.dushen.model.counts import counts

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
FORMAT_DATE = '%Y%m%d'

bonus_count = 0


def run(count=5):
    """ count : default foreach 5 counts """

    weekday_dlt = [1, 3, 6, 5]
    weekday_ssq = [2, 4, 7, 5]

    today = datetime.date.today()
    weekday = today.isoweekday()
    if weekday in weekday_dlt:
        df = utils.read_csv_data('dlt')
        no = max(df['no'].to_list()) + 1
        if weekday == 5:
            today = today + datetime.timedelta(days=1)
        l_model.dlt(no, int(today.strftime(FORMAT_DATE)))

        # probability.dlt()

        red1 = df['red1'].to_list()
        red1.reverse()
        red2 = df['red2'].to_list()
        red2.reverse()
        red3 = df['red3'].to_list()
        red3.reverse()
        red4 = df['red4'].to_list()
        red4.reverse()
        red5 = df['red5'].to_list()
        red5.reverse()
        blue1 = df['blue1'].to_list()
        blue1.reverse()
        blue2 = df['blue2'].to_list()
        blue2.reverse()

        data = []
        for i in range(0, count):
            row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(blue1[i]), str(blue2[i])]
            data.append(','.join(row))

        data.reverse()
        bonus = counts.dlt2One(data)

        if '2,27,30,34,35,9,12' == bonus:
            print(globals()['bonus_count'], '::', bonus)
        else:
            globals()['bonus_count'] = globals()['bonus_count'] + 1
            run(count)

    today = datetime.date.today()
    weekday = today.isoweekday()
    if weekday in weekday_ssq:
        df = utils.read_csv_data('ssq')
        no = max(df['no'].to_list()) + 1
        if weekday == 5:
            today = today + datetime.timedelta(days=2)
        l_model.ssq(no, int(today.strftime(FORMAT_DATE)))

        # probability.ssq()

        red1 = df['red1'].to_list()
        red1.reverse()
        red2 = df['red2'].to_list()
        red2.reverse()
        red3 = df['red3'].to_list()
        red3.reverse()
        red4 = df['red4'].to_list()
        red4.reverse()
        red5 = df['red5'].to_list()
        red5.reverse()
        red6 = df['red6'].to_list()
        red6.reverse()
        blue1 = df['blue1'].to_list()
        blue1.reverse()

        data = []
        for i in range(0, count):
            row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(red6[i]), str(blue1[i])]
            data.append(','.join(row))

        data.reverse()
        bonus = counts.ssq2One(data)
        if '5,8,16,17,21,25,12' == bonus:
            print(globals()['bonus_count'], '::', bonus)
        else:
            globals()['bonus_count'] = globals()['bonus_count'] + 1
            run(count)
