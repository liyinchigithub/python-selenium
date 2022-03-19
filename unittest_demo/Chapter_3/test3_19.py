import os

#返回指定目录下的所有文件和目录名
a = os.listdir(os.getcwd()) # ['allure-2.17.2', 'conftest.py', '.DS_Store', 'pytest.ini', 'requirements.txt', '.pytest_cache', '__pycache__', '.history', 'README.md', 'unittest_demo', 'download_file', '.gitignore', 'webdriver_init.py', 'log', 'save_images', 'report', 'chromedriver', '.git', 'logging_init.py', 'src']
print(a)

for i in list(a):
    if os.path.isfile("/Users/liyinchi/workspace/python/python-selenium/"+i):
        print("{}是文件".format(i))
    elif os.path.isdir("/Users/liyinchi/workspace/python/python-selenium/"+i):
        print("{}是文件夹".format(i))
        

#创建一个目录。
os.mkdir('D:\\abc')
#删除一个空目录。若目录中有文件，则无法删除。
os.rmdir('D:\\abc')
#可以生产多层递归目录。如果目录全部存在，则创建目录失败。
os.makedirs('D:\\abc\\def\\')
# 可以删除多层递归的空目录，若目录中有文件则无法删除。
os.removedirs('D:\\abc\\def\\')
# 改变当前目录，到指定目录中去。
os.chdir('D:\\abc\\def\\')
# 重命名目录名或文件名。命名后的文件名如果存在，则重命名失败。
os.rename('D:\\abc\\def', 'D:\\abc\\xyz')

# 返回文件名
os.path.basename('D:\\abc\\def\\a.txt')
# 返回文件路径
os.path.dirname('D:\\abc\\def\\a.txt')
# 获得文件大小，如果name是目录返回0L；
os.path.getsize('D:\\abc\\def\\a.txt')
# 获得绝对路径
os.path.abspath('D:\\abc\\def\\a.txt')
# 连接目录与文件名或目录
os.path.join('D:\\abc\\def\\','a.txt')
