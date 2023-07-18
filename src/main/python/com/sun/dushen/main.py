# - *- coding: utf- 8 - *-
import sys

from com.sun.dushen.model import model
from com.sun.dushen.pixiu import pixiu

args = sys.argv[1:]
"""  
    args
      0: 爬虫用
      1: 模型用
"""
# 爬数据
if len(args) == 0 or args[0] == 'RUN':
    pixiu.run()

# 随机数模型
if len(args) == 2 and int(args[1]) > 0:
    if int(args[1]) <= 5:
        # 默认模型
        model.run()
    else:
        # 指定随机数模型
        model.run_ssq2(int(args[1]))


# TODO
model.run_analysis()
