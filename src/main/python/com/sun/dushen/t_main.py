import math
import os
import sys
from concurrent import futures

from com.sun.dushen.common import utils
from com.sun.dushen.model.counts import counts
from com.sun.dushen.pixiu import pixiu

args = sys.argv[1:]


def main():
    # 爬数据
    if len(args) == 0 or args[0] == 'RUN':
        pixiu.run()

    df = utils.read_csv_data('ssq')
    thread_count = (os.cpu_count() + 1) * 2
    data_split_size = math.ceil(len(df) / thread_count)

    body = []
    with futures.ProcessPoolExecutor(thread_count) as executor:
        fs = []
        for i in range(0, thread_count):
            end = data_split_size * i + data_split_size
            if end > len(df):
                end = len(df)

            f = executor.submit(counts.sub_ssq, data_split_size * i, end, df)
            fs.append(f)

        for f in futures.as_completed(fs):
            d = f.result()[0].split(',')
            row = {
                'no': d[0],
                'date': d[1],
                'red1': d[2],
                'red2': d[3],
                'red3': d[4],
                'red4': d[5],
                'red5': d[6],
                'red6': d[7],
                'blue1': d[8],
                'count': d[9],
            }
            body.append(row)

    counts.write_counts('ssq', ['no', 'date', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue1', 'count'], body)


if __name__ == '__main__':
    main()
