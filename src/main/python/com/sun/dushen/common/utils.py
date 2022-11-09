import os
import random


def root():
    r"""get main directory ."""
    return os.path.abspath(r'../../../..')


def resources_path():
    r"""get resources directory ."""

    return root() + r'/resources'


def randoms(scope, count):
    return random.sample(range(1, scope + 1), count)


# return string randoms
def randoms_s(scope, count):
    r = random.sample(range(1, scope + 1), count)
    result = []
    for i in r:
        if i < 10:
            result.append(str(i).zfill(2))
        else:
            result.append(str(i))

    return result
