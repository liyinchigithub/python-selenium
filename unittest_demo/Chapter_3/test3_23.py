import os
#通过open打开文件:第一个参数为文件名；第二个参数为模式；第三个参数为编码方式；
f = open(os.getcwd()+"/unittest_demo/Chapter_3/test3_1.py","r",encoding='utf8')
# 通过read读取文件全部内容
data = f.read()
print(data) # 打印
f.close() # 关闭文件