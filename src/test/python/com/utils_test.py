import unittest

from com.sun.dushen.common import utils


class MyTestCase(unittest.TestCase):
    def test_something(self):
        r = ','.join(str(s) for s in sorted(utils.randoms_s(35, 5), reverse=False))
        b = ','.join(str(s) for s in sorted(utils.randoms_s(12, 2), reverse=False))
        t = r + ',' + b
        print('test ::', t)
        self.assertNotEqual(t, '')


if __name__ == '__main__':
    unittest.main()
