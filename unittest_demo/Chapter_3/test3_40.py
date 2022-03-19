import csv,os

with open(os.getcwd()+"/unittest_demo/Chapter_3/my_csv_1.csv", 'r', encoding='utf8') as f:
    data = csv.reader(f)
    print(data)
    for i in data:
        print(i)