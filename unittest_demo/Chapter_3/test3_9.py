def power(x, n):
    '''定义一个函数，计算x的n次方'''
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

if __name__ == '__main__':
    print(power(3,2))
    print(power(2,3))
