import json
import math
import numpy as np


def find_interseting(keywords: list, dic: dict):
    '''求多个函数的交集'''
    keywords_list = []  # 得到相应单词的文档列表
    for keyword in keywords:
        if keyword in dic.keys():
            keywords_list.append(dic[keyword])
    interset = keywords_list[0]
    for key in keywords_list:
        interset = find_interseting_core(key, interset)
    # print(interset)
    return interset


def find_interseting_core(key_list: list, key_list_1: list):
    '''求两个函数的交集'''
    answer = []
    length = len(key_list)
    pos = 0
    length1 = len(key_list_1)
    pos1 = 0;
    if length == 0 or length1 == 0: return []
    while pos != length or pos1 != length1:  # 这里不能减一
        if key_list[pos][0] == key_list_1[pos1][0]:
            answer.append(key_list[pos])
            pos = pos + 1
            pos1 = pos1 + 1
        elif key_list[pos][0] < key_list_1[pos1][0]:
            pos = pos + 1
        else:
            pos1 = pos1 + 1
    return answer


def sort_doc(interset: list, dic: dict, keyword: list, N: int):
    '''计算每个交集文档的得分'''
    score = []

    for doc in interset:
        docID = doc[0]
        # 计算idf
        idf = []  # 保存每个单词的idf
        for key in keyword:
            idf_1 = 0
            for item in dic[key]:
                idf_1 = idf_1 + item[1]
            idf.append(1 + math.log10(N / idf_1))
        num = 0
        i = 0  # 保存单词的序列号
        for key in keyword:
            temp = 0
            tf = 0
            for docs in dic[key]:
                if docs[0] == docID:
                    tf = docs[1]
                    break
            temp = (1 + math.log10(tf)) * idf[i]
            num = num + temp
            i = i + 1

        score.append([docID, num])
    return score


dic_filename = 'dic.txt'
list_filename = 'list.txt'
with open(dic_filename) as file_objet:
    dic = json.load(file_objet)
N = input("请输入常数N:\n")
N = int(N)
keyword = input("请输入查询的单词(空格分隔):\n")
keyword = keyword.lower().split()
interset = find_interseting(keyword, dic)
# print(str(interset)+'\n')
score = sort_doc(interset, dic, keyword, N)
# print(str(score)+'\n')
temp = []
for l in score:
    temp.append(l[1])
# print(str(temp)+'\n')
x = np.array(temp)
y = np.argsort(-x)
# print(y)
for l in y:
    print("d" + str(score[l][0]) + '\n')
