from com.sun.dushen.lottery import l_model, probability
from com.sun.dushen.pixiu import ssq, dlt
from com.sun.dushen.counts import counts

# ssq.run()
# dlt.run()

l_model.dlt(22126, 20221105)
probability.dlt()
counts.dlt2One([
    '4,15,16,20,21,4,5',
    '4,15,17,19,25,6,12',
    '2,20,28,29,30,7,10',
    '2,4,11,25,30,6,12',
    '3,7,14,16,19,1,11',
])

# l_model.ssq(22126, 20221103)
# probability.ssq()
# counts.ssq2One(['12,17,22,27,30,31,2',
#                 '6,8,17,19,24,28,5',
#                 '10,13,16,20,21,25,5',
#                 '5,10,13,18,24,26,1',
#                 '2,3,7,12,20,31,16',
#                 ])
