import re


def split_file(filename):
    d = list()
    with open(filename, encoding='utf-8') as file_obj:
        for line in file_obj.readlines():
            temp = line.rstrip().lower()
            d.append(re.split(r'[\s.]', temp))
    return d


def find(keyword_1, d):
    i = 1
    for a in d:
        if keyword_1 in a:
            print('d' + str(i))
        i = i + 1


while True:
    keyword = input('请输入查询关键字,输入q退出')
    if keyword == 'q':
        break
    d = split("data.txt")
    find(keyword.lower(), d)
