#Define a bunch off attributes & functions inside a class, allows another class to inherit all of those attributes & functions
#When naming class start with captial letter
class Mammal:
    def walk(self):
        print('Walk')
class Dog(Mammal):
    pass #so that there won't be error
class Cat(Mammal):
    def meow(self):
        print('Meow')
cat1 = Cat()
cat1.meow()
dog1 = Dog()
dog1.walk()

#Generating random number

import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

dice = Dice()
print(dice.roll())