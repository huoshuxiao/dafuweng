# 计算中奖号码的随机次数，生成随机号码
import math

from com.sun.dushen.common import utils


# 进N出N
def ssq(bonuses):
    for bonus in bonuses:
        print(bonus)
        do = True
        i = 0
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms_s(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms_s(16, 1), reverse=False))
            t = r + ',' + b
            if bonus == t:
                do = False
        print(i)

        while i > 0:
            i = i - 1
            r = ','.join(str(s) for s in sorted(utils.randoms_s(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms_s(16, 1), reverse=False))
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
            r = ','.join(str(s) for s in sorted(utils.randoms_s(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms_s(16, 1), reverse=False))
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
        r = ','.join(str(s) for s in sorted(utils.randoms_s(33, 6), reverse=False))
        b = ','.join(str(s) for s in sorted(utils.randoms_s(16, 1), reverse=False))
        t = r + ',' + b
    print(t)


# 进N出N
def dlt(bonuses):
    for bonus in bonuses:
        print(bonus)
        do = True
        i = 0
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms_s(35, 5), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms_s(12, 2), reverse=False))
            t = r + ',' + b
            if bonus == t:
                do = False
        print(i)

        while i > 0:
            i = i - 1
            r = ','.join(str(s) for s in sorted(utils.randoms_s(35, 5), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms_s(12, 2), reverse=False))
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
            r = ','.join(str(s) for s in sorted(utils.randoms_s(35, 5), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms_s(12, 2), reverse=False))
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
        r = ','.join(str(s) for s in sorted(utils.randoms_s(35, 5), reverse=False))
        b = ','.join(str(s) for s in sorted(utils.randoms_s(12, 2), reverse=False))
        t = r + ',' + b
    print(t)
