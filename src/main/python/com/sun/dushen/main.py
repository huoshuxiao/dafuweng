import sys

from com.sun.dushen.model import model
from com.sun.dushen.pixiu import pixiu

args = sys.argv[1:]
"""  
    args
      0: 爬虫用
      1: 模型用
"""
if args[0] == 'NOT-SKIP' or len(args) == 0:
    pixiu.run()

if len(args) == 1:
    model.run()
else:
    model.run(int(args[1]))
