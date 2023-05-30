
# Jaccard相似度通过计算两个集合之间的交集和并集之间的比率来衡量相似性。
def similarity_score(arr1, arr2):
    set1 = set(arr1[0].split(","))
    set2 = set(arr2[0].split(","))
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    score = len(intersection) / len(union)
    return score


text1 = [["04,09,19,20,21,26"]]
text2 = ["04,09,19,20,21,26"]

score = similarity_score(text1[0], text2)
print("相似度得分:", score)
