import os
f = open(os.getcwd()+"/unittest_demo/Chapter_3/1.txt","r",encoding='utf8')
# 通过readlines读取全部内容，返回列表
data3 = f.readlines()
print("readlines对应的结果: {}".format(data3))
f.close() # 关闭文件