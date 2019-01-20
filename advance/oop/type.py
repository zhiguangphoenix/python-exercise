class Animal(object):
    def run(self):
        print('run')

class Dog(Animal):
    def run(self):
        print('dog run...')

class Cat(Animal):
    def run(self):
        print('cat run...')

animal = Animal()
dog = Dog()

print(isinstance(animal, Animal))
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))