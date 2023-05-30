import csv

from com.sun.dushen.common import utils


# Jaccard相似度通过计算两个集合之间的交集和并集之间的比率来衡量相似性。
def similarity_score(arr1, arr2):
    set1 = set(arr1.split(","))
    set2 = set(arr2.split(","))
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    score = len(intersection) / len(union)
    return score


def ssq():
    df = utils.read_csv_data('ssq')
    red1 = df['red1'].to_list()
    red2 = df['red2'].to_list()
    red3 = df['red3'].to_list()
    red4 = df['red4'].to_list()
    red5 = df['red5'].to_list()
    red6 = df['red6'].to_list()

    blue1 = df['blue1'].to_list()

    date = df['date'].to_list()

    redData = []
    blueData = []
    for i in range(0, len(red1)):
        row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(red6[i])]
        redData.append(','.join(row))

        row = [str(blue1[i])]
        blueData.append(','.join(row))

    result = []
    # 现有号码相似度
    for i in range(1, len(redData)):
        redText1Array = redData[0:i]
        redText2 = redData[i]

        blueText1Array = blueData[0:i]
        blueText2 = blueData[i]

        for j in range(0, len(redText1Array)):
            text1 = redText1Array[j] + ',B' + blueText1Array[j]
            text2 = redText2 + ',B' + blueText2
            score = similarity_score(text1, text2)
            print("日期：{} 当期号码：{} 池号码：{} 相似度得分:{} ".format(date[i], redText2, redText1Array[j], score))

            data = {
                'date': date[i],
                'current': text2.replace('B', ''),
                'pool': text1.replace('B', ''),
                'score': score,
            }
            result.append(data)

    write(result)


def write(body):
    r"""create ssq data csv. """

    # name of csv file
    filename = utils.resources_path() + r'/data/ssq_similarity.csv'

    # field names
    fields = ['date', 'current', 'pool', 'score']

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        writer.writerows(body)


ssq()
