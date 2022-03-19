import datetime

# 输出当前日期
print(datetime.datetime.now())
# 输出当前日期的下一天
print(datetime.datetime.now() + datetime.timedelta(days=1))
# 输出当前日期的下一个小时
print(datetime.datetime.now() + datetime.timedelta(hours=1))
# 输出当前时间的下一分钟
print(datetime.datetime.now() + datetime.timedelta(minutes=1))
# 输出当前时间的下一秒
print(datetime.datetime.now() + datetime.timedelta(seconds=1))
