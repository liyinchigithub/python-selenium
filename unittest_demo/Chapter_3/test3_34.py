import json,os

with open(os.getcwd()+"/unittest_demo/Chapter_3/1.txt",'r') as f:
    print(type(f))
    dic = json.load(f)
    print(dic)
    print(type(dic))