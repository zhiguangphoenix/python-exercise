class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def log(self):
        print('%s: %s' % (self.name, self.score))

s1 = Student('S1', 11)
s1.log()
s1.height = 188
print(s1.name)
print(s1.height)