import os

# 假如我想拼接一个当前文件同级目录里面一个aa.py文件
cur_path = os.getcwd()  # 获取当前目录
print(cur_path)
file = cur_path + os.sep + 'aa.py' # 通过sep来取适合当前操作系统的分隔符
print(file)
file_name = os.path.basename('unittest_demo/Chapter_3/test3_18.py')  # 获取当前文件名 输出： test3_18.py
print(file_name)
dir_name = os.path.dirname('unittest_demo/Chapter_3/test3_18.py')  # 获取当前文件所在路径 输出： unittest_demo/Chapter_3
print(dir_name)
file_split = os.path.split('unittest_demo/Chapter_3/test3_18.py')  # 获取当前文件所在路径 输出：('unittest_demo/Chapter_3', 'test3_18.py'
print(file_split)
file_format = os.path.splitext('unittest_demo/Chapter_3/test3_18.py')  # 获取当前文件格式 输出：('unittest_demo/Chapter_3/test3_18', '.py')
print(file_format)
print(file_format[1])