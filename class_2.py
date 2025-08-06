class Animals:
    def __init__(self, name, species, age, sound, zoo_name):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self.zoo_name = zoo_name

    def make_sound(self):
        print(f'the {self.name} makes the {self.sound} sound')

    def info(self):
        print(f'this is a {self.name} from {self.zoo_name} zoo')
        print(f'they are {self.age} yo. and is fro {self.species} species')

    def __str__(self):
        return (f'this is a {self.name} from {self.zoo_name} zoo. They are {self.age} yo'
                f'. and is from {self.species} species.')


class Birds(Animals):
    def __init__(self, name, species, age, sound, zoo_name, wing_span):
        Animals.__init__(self, name, species, age, sound, zoo_name)
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self.zoo_name = zoo_name
        self.wing_span = wing_span

    def make_sound(self):
        print(f'this bird makes a {self.sound} noise')


lion = Animals('lion', 'feliformia', 12, 'roar', 'San diego')
crow = Birds('crow', 'birds', 100, 'ka-ka', 'New york', 30)

lion.make_sound()
lion.info()
print(lion)
print(crow)
crow.make_sound()
