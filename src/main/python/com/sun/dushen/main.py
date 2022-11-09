import sys

from com.sun.dushen.lottery import l_model, probability
from com.sun.dushen.pixiu import ssq, dlt
from com.sun.dushen.counts import counts

# ssq.run()
# dlt.run()


r"""args 
    0 is 彩票类型
"""
args = sys.argv[1:]
if 'dlt' == args[0]:
    l_model.dlt(22128, 20221109)
    probability.dlt()
    counts.dlt2One([
                    '2,20,28,29,30,7,10',
                    '2,4,11,25,30,6,12',
                    '3,7,14,16,19,1,11',
                    '4,5,8,22,35,1,3',
                    '2,3,8,9,20,4,10',
                    ])
else:
    l_model.ssq(22129, 20221110)
    probability.ssq()
    counts.ssq2One([
                    '5,10,13,18,24,26,1',
                    '2,3,7,12,20,31,16',
                    '1,13,15,17,26,33,13',
                    '3,4,9,10,29,33,13',
                    '3,12,18,24,27,29,1',
                    ])
