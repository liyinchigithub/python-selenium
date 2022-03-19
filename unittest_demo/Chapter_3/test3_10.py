def power(x, n=2):
    '''定义个一个函数，计算x的n次方，当n未传递时，n=2'''
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

if __name__ == '__main__':
    # print(power(3,2))
    # print(power(2,3))
    print(power(3))
    print(power(3,2))