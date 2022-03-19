import json,os
file = os.getcwd()+"/unittest_demo/Chapter_3/login_account.json"

with open(file, 'r') as f:
    users = json.load(f)
    print(type(f))
    print(type(users))
    print(users)

for user in users:
    print(user)
    # name = users[user]['name']
    # password = users[user]['password']
    # print(name,password)
