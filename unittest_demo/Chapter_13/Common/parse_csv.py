import csv

'''
返回嵌套列表，类似：[['admin', 'error', '0'], ['admin', 'rootroot', '1']]
'''
def parse_csv(file):
    mylist = []
    with open(file, 'r', encoding='utf8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0] # 删除标题那行数据
        return mylist


if __name__ == '__main__':
    data = parse_csv('my_csv_1.csv')
    print(data)
