class Animal:

    sound = None
    dead = False

    def __init__(self, class_, lifespan, food, gender, age):
        self.class_ = class_
        self.lifespan = lifespan
        self.food = food 
        self.gender = gender
        self.age = age

    def __str__(self): 
        return f'{self.class_}, {self.food}, {self.gender}, {self.age} years old'

    def __repr__(self):
        return f'{type(self).__name__} -> {self.food} {self.class_} that lives for ~{self.lifespan} years'

    def speak(self):
        if self.sound is None:
            print('This animal does not make a particular sound')
        else:
            print(f'{self.sound}, {self.sound}!')

    def die(self):
        self.dead = True
        print('Unfortunately this animal died')

    def birthday(self):
        if not self.dead:
            self.age += 1
        else:
            print("It died, it can not level up anymore")

class Dog(Animal):

    def __init__(self, lifespan, gender, age, breed, name, no_of_legs, class_='mammal', food='omnivore'):
        super().__init__(class_, lifespan, food, gender, age)
        self.breed = breed
        self.name = name
        self.no_of_legs = no_of_legs
        self.sound = 'Woof'

    def bark(self):
       return self.speak()

    def get_details(self):
        return f'{self.name} is a {self.gender} {self.breed} aged {self.age}'

    def give_birth(self, no_of_kids):
        if self.gender is 'female':
            print(f'{self.name} gave birth to {no_of_kids} puppies')
        else:
            print(f'{self.name} is a male, it can not give birth')

    def get_age_in_dog_years(self):
        return f'The age in dog years for {self.name} is {self.age*7}'

cow = Animal('mammal', 20, 'herbivore', 'female', 5)
print(f'Cow: {cow}')
print(repr(cow))
cow.sound = 'Moo'
cow.speak()
cow.die()

print('#' * 20)

pigeon = Animal('bird', 3, 'omnivore', 'male', 1)
print(f'Pigeon: {pigeon}')
print(repr(pigeon))
pigeon.speak()

print('#' * 20)

dog1 = Dog(15, 'male', 12, 'cane corso', 'Thor', 4)
print(repr(dog1))
dog1.give_birth(3)
dog1.birthday()
print('Happy birthday to {}! It is now {} years old'.format(dog1.name, dog1.age))
dog1.die()
dog1.birthday()

print('#' * 20)

dog2 = Dog(12, 'female', 10, 'poodle', 'Jojo', 3)
print(dog2.get_details())
dog2.bark()
dog2.give_birth(5)
print(dog2.get_age_in_dog_years())
dog2.birthday()
print('Happy birthday to {}! It is now {} years old'.format(dog2.name, dog2.age))

