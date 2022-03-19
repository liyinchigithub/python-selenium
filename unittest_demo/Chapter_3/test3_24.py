import os
f = open(os.getcwd()+"/unittest_demo/Chapter_3/1.txt","r",encoding='utf8')
# 通过read读取文件全部内容
data1 = f.read()
print("read对应的结果: {}".format(data1))
f.close() # 关闭文件