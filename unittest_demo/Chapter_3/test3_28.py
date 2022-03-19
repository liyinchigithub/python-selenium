import os
with open(os.getcwd()+"/unittest_demo/Chapter_3/3.txt","w",encoding='utf8') as f:
    # 列表
    data = ['name\n','age\n','sex']
    # 按行写入
    f.writelines(data)
