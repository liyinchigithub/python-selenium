import time
# 输出年月日，以斜杠分隔
print(time.strftime('%Y/%m/%d',time.localtime(time.time())))

# 显示年月日时分秒，中间无分隔，常用作保存日志的文件名
print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))

