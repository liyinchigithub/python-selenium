import os
with open(os.getcwd()+"/unittest_demo/Chapter_3/1.txt", "r") as f:
    data = f.read()
    print(data)