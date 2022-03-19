def print_score(std):
    print('{}: {}'.format(std['name'],std['score']))

if __name__ == '__main__':
    std1 = {'name': 'Michael', 'score': 98}
    std2 = {'name': 'Bob', 'score': 81}
    print_score(std1)
    print_score(std1)