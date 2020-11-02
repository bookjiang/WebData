import  re
import json
def split_file(filename):
    """将文本切割成列表,json"""
    d = list()
    with open(filename, encoding='utf-8') as file_obj:
        for line in file_obj.readlines():
            temp = line.rstrip().lower()
            d.append(re.split(r'[\s.]', temp))
    with open('list.txt','w',encoding='utf-8') as file_obj1:
        json.dump(d,file_obj1)
    return d


def create_dic(d):
    """得到字典存储,同时存下单词在文档中的频率，json"""
    '''得到set集合'''
    dic={}
    keywords = set()
    for d1 in d:
        a = set(d1)
        keywords = keywords | a
    keywords.remove('')  #前面正则多分了一个空格，这里处理一下
    keywords_1=frozenset(keywords)
    #print(keywords_1)
    for keyword in keywords_1 :
        dic[keyword]=[]
        i=1  #保存句子序列号
        for d1 in d:
            if keyword in d1 :
                #如果在则计算一下频率
                j=0
                for k in d1 :
                    if keyword==k :
                        j=j+1
                list_key=[i,j]
                #dic[keyword].extend(str(i))
                dic[keyword].append(list_key)
            i=i+1
    #序列化字典
    with open('dic.txt','w') as file_object:
        json.dump (dic, file_object)
    return dic

def find(keyword,dic:dict):
    if keyword in dic.keys():
        print(dic[keyword])

keyword=input("请输入查询的关键字，输入q结束")
d=split_file('data.txt')
dic=create_dic(d)
find(keyword,dic)