import json,os

dict1 = {"name":"storm","age": 30}
print(dict1)
print(type(dict1))

# 将字典数据写入txt文件
with open(os.getcwd()+"/unittest_demo/Chapter_3/1.txt","w") as f:
    j1 = json.dump(dict1,f)
    print(j1)
    print(type(j1))