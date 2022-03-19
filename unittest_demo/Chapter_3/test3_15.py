class Student(object):
    '''定义一个Student对象，包含name和score两个属性'''
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{}: {}' .format(self.name, self.score))

if __name__ == '__main__':
    storm = Student('Storm', 59)
    sk = Student('SK', 87)
    storm.print_score()
    sk.print_score()
