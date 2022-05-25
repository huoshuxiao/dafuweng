import pandas

from com.sun.dushen.common import utils


def dlt():
    filename = utils.resources_path() + r'/data/dlt.csv'
    df = pandas.read_csv(filename)
    red = df['red1'].to_list() + df['red2'].to_list() + df['red3'].to_list() + df['red4'].to_list() + df['red5'].to_list()
    counts = len(df['red1'].to_list())

    red_probability = dict()
    # cal
    for i in range(1, 36):
        red_probability.setdefault(i, red.count(i) / counts)

    red_values = list(red_probability.values())
    for s in sorted(red_values, reverse=True):
        for k, v in red_probability.items():
            if s == v:
                print(v, k)
                red_probability.pop(k)
                break

    blue = df['blue1'].to_list() + df['blue2'].to_list()
    blue_probability = dict()
    # cal
    for i in range(1, 13):
        blue_probability.setdefault(i, blue.count(i) / counts)

    blue_values = list(blue_probability.values())
    for s in sorted(blue_values, reverse=True):
        for k, v in blue_probability.items():
            if s == v:
                print('blue', v, k)
                blue_probability.pop(k)
                break
