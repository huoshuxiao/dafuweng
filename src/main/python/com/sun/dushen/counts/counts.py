# 计算中奖号码的随机次数，生成随机号码
import time

from com.sun.dushen.common import utils


def ssq(bonuses):
    for bonus in bonuses:
        # print(bonus)
        do = True
        i = 0
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
            t = r + ',' + b
            # print(t)
            if bonus == t:
                do = False
        print(i)
        # time.sleep(1)

        while i > 0:
            i = i - 1
            # print(i)
            r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
            t = r + ',' + b
        print(t)
        # time.sleep(1)


def dlt(bonuses):
    for bonus in bonuses:
        # print(bonus)
        do = True
        i = 0
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms(35, 5), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(12, 2), reverse=False))
            t = r + ',' + b
            # print(t)
            if bonus == t:
                do = False
        print(i)
        # time.sleep(1)

        while i > 0:
            i = i - 1
            # print(i)
            r = ','.join(str(s) for s in sorted(utils.randoms(35, 5), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(12, 2), reverse=False))
            t = r + ',' + b
        print(t)
        # time.sleep(1)
