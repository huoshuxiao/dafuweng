import csv
import os
import random

import pandas


def root():
    r"""get main directory ."""
    return os.path.dirname(os.path.abspath(__file__ + r'../../../../../..'))


def resources_path():
    r"""get resources directory ."""

    return root() + r'/resources'


def read_csv(file_name):
    filename = resources_path() + r'/data/{}.csv'.format(file_name)
    return pandas.read_csv(filename)


def write_csv(file_name, file_fields, body):
    r"""create ssq data csv. """

    # name of csv file
    filename = resources_path() + r'/data/{}.csv'.format(file_name)

    # field names
    fields = file_fields

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        writer.writerows(body)


def randoms(scope, count):
    return random.sample(range(1, scope + 1), count)


# return string randoms
def randoms_s(scope, count):
    r = randoms(scope, count)
    result = []
    for i in r:
        if i < 10:
            result.append(str(i).zfill(2))
        else:
            result.append(str(i))

    return result
