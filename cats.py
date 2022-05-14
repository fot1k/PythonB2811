import random
from time import sleep

class Cat:
    def __init__(self, n):
        self.name = n
    def run(self):
        print(f'{self.name} бежит')
    def jump(self):
        print(f'{self.name} прыгает')
    def eat(self):
        print(f'{self.name} кушает')
    def sleep(self):
        print(f'{self.name} спит')
    def murmur(self):
        print(f'{self.name} мурчит')
    def carapaetsa(self):
        print(f'{self.name} царапается')
    def kuskus(self):
        print(f'{self.name} делает кусь')
    def play(self):
        print(f'{self.name} играется')
    def shipit(self):
        print(f'{self.name} шипит')
    def maukaet(self):
        print(f'{self.name} мяукает')

cats = []
cats.append(Cat('Murzik'))
cats.append(Cat('Oleg'))
cats.append(Cat('Barsik'))
cats.append(Cat('Cotan'))
cats.append(Cat('Ryzhyk'))
cats.append(Cat('Vasya'))
cats.append(Cat('Cherniy'))

while True:
    cat = random.choice(cats)
    actions = [cat.eat, cat.jump, cat.run, cat.sleep, cat.murmur, cat.carapaetsa, cat.kuskus, cat.play, cat.shipit, cat.maukaet]
    action = random.choice(actions)
    action()
    sleep(0.5)