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
