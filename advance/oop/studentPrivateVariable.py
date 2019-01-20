class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def log(self):
        print('%s: %s' % (self.__name, self.__score))

s = Student('czg', 24)
s.log()
s.__name = 'zg'
print(s.__name)

