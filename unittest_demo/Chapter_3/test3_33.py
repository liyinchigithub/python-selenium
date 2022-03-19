import json

# str1是单引号包裹的字符串
str1 = '{"name":"storm","age": 30}'
print(str1)
print(type(str1))

# loads转成字典
dic = json.loads(str1)
print(dic)
print(type(dic))