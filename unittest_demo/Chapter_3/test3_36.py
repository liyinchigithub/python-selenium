import json,os

file = os.getcwd()+"/unittest_demo/Chapter_3/myarray.json"

with open(file,'r') as f:
    ss = json.load(f) # 字符串转字典

for s in ss:
    print(s)
    print(s["name"])
    print(s["age"])