import yaml,os

with open(os.getcwd()+"/unittest_demo/Chapter_3/my_yaml_2.yml", 'r', encoding='utf8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
