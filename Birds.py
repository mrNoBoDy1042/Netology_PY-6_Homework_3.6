class Birds:
    name = ''
    age = 0
    weight = 0
    top_speed = 0

    def say_my_name(self):
        return 'My name is {}'.format(self.name)

    def check_params(self):
        return 'My age is {0} and my weight is {1} and my max speed is {2} km\\h'\
            .format(self.age, self.weight, self.top_speed)


class Duck(Birds):
    def __init__(self, name, age, weight, speed):
        self.name = name
        self.age = age
        self.weight = weight
        self.top_speed = speed


class Goose(Birds):
    def __init__(self, name, age, weight, speed):
        self.name = name
        self.age = age
        self.weight = weight
        self.top_speed = speed


class Hen(Birds):
    def __init__(self, name, age, weight, speed):
        self.name = name
        self.age = age
        self.weight = weight
        self.top_speed = speed

goose_Google = Goose('Google', 14, 25, 50)
print(goose_Google.check_params())

duck_Yandex = Duck('Yandex', 13, 19, 55)
print(duck_Yandex.say_my_name())

hen_Bing = Hen('Bing', 9, 10, 25)
