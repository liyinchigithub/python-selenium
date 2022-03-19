import json

dict1 = {"name":"storm","age": 35}
print(dict1)
print(type(dict1))

# dumps将字典转为字符串
j1 = json.dumps(dict1)
print(j1)
print(type(j1))

