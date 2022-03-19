class Animals(object):
    def run(self):
        print('Animals can run')

class Dog(Animals):
    def run(self):
        print('Dog can run')

    def say(self):
        print("汪汪汪")

class Cat(Animals):
    def run(self):
        print('Cat can run')

if __name__ == '__main__':
    Dog().run()
    Dog().say()
    Cat().run()
