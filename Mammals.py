class Mammal:
    name = ''
    age = 0
    weight = 0
    sound = ''

    def say_my_name(self):
        return 'My name is {}'.format(self.name)

    def check_params(self):
        return 'My age is {0} and my weight is {1}'.format(self.age, self.weight)


class Cow(Mammal):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.sound = 'Mooooo!'

    def make_sound(self):
        return self.sound


class Goat(Mammal):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.sound = 'Baaaaahh'

    def make_sound(self):
        return self.sound


class Sheep(Mammal):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.sound = ''

    def make_sound(self):
        return self.sound


class Pig(Mammal):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.sound = ''

    def make_sound(self):
        return self.sound


cow_Igor = Cow('Igor', 16, 120)
print(cow_Igor.say_my_name())
print(cow_Igor.make_sound())

goat_Ira = Goat('Lena', 20, 60)
print(goat_Ira.check_params())

sheep_Dave = Sheep('Dave', 20, 100)

pig_Tim = Pig('Tim', 30, 150)

