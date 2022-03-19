import os
with open(os.getcwd()+"/unittest_demo/Chapter_3/test3_30.json", 'r', encoding='utf8') as f:
    data = f.read()
    print(type(data))