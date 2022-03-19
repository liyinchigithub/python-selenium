import os
f = open(os.getcwd()+"/unittest_demo/Chapter_3/1.txt","r",encoding='utf8')
# 通过readline读取一行内容
data2 = f.readline()
print("readline对应的结果: {}".format(data2))
f.close() # 关闭文件