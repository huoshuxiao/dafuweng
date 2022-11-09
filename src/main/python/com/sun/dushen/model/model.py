import datetime

from com.sun.dushen.model.lottery import probability, l_model
from com.sun.dushen.model.counts import counts


def run():
    weekday_dlt = [1, 3, 6, 5]
    weekday_ssq = [2, 4, 7, 5]

    date = datetime.date
    today = date.today()
    weekday = today.isoweekday()

    if weekday in weekday_dlt:
        l_model.dlt(22128, 20221109)
        probability.dlt()
        counts.dlt2One([
            '02,20,28,29,30,07,10',
            '02,04,11,25,30,06,12',
            '03,07,14,16,19,01,11',
            '04,05,08,22,35,01,03',
            '02,03,08,09,20,04,10',
        ])

    if weekday in weekday_ssq:
        l_model.ssq(22129, 20221110)
        probability.ssq()
        counts.ssq2One([
            '05,10,13,18,24,26,01',
            '02,03,07,12,20,31,16',
            '01,13,15,17,26,33,13',
            '03,04,09,10,29,33,13',
            '03,12,18,24,27,29,01',
        ])
