import sys

from com.sun.dushen.model import model
from com.sun.dushen.pixiu import pixiu

args = sys.argv[1:]
if args[0] == 'NOT-SKIP' or len(args) == 0:
    pixiu.run()

model.run()
