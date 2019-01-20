class Animal(object):
    def run(self):
        print('run')

class Dog(Animal):
    def run(self):
        print('dog run...')

class Cat(Animal):
    def run(self):
        print('cat run...')

class Fake(object):
    def run(self):
        print('fake run...')

def run2(Animal):
    Animal.run()

animal = Animal()
dog = Dog()
cat = Cat()
fake = Fake()

run2(animal)
run2(dog)
run2(cat)
run2(fake)