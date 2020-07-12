class Vehicles(object):

    def __init__(self, producer_name, model_of_the_car, number_of_dors, age, color):
        self.producer_name = producer_name
        self.model_of_the_car = model_of_the_car
        self.number_of_dors = number_of_dors
        self.age = age
        self.color = color

    def car_description(self):
         return f'The Car {self.producer_name} {self.model_of_the_car} has {self.color} and is from {self.age}'
         
    def is_to_old(self):
        return self.age < 1999

    def print_welcome_message():
        print('Hello and welcome to our store')

class Car(Vehicles):

    def __init__(self,producer_name, model_of_the_car, number_of_dors, age, color,type_of_the_car, motor_of_the_car):
        self.type_of_the_car = type_of_the_car
        self.motor_of_the_car = motor_of_the_car
        super().__init__(producer_name, model_of_the_car, number_of_dors, age, color)

    def __str__(self):
        return '{} {}, {}, {}, {}, {}'.format(
            self.producer_name, self.model_of_the_car, self.number_of_dors, self.age, self.color, self.type_of_the_car)

    def motor_option(self, client_preference):
        return self.type_of_the_car == client_preference


    
cars =[
    Car('Renault', 'Laguna', 4, 2005, 'grey','Sedan', 1.6),
    Car('Volkswagen', 'Golf', 2, 2007, 'white','Hatchback', 2.0),
    Car('Volkswagen', 'Polo', 4, 2011, 'blue', 'Hatchback ', 1.2),
    Car('Audi', 'TT', 2, 2015, 'red', 'Coupe', 2.1),
    Car('Mercedes', 'Cobra', 4, 1978, 'yellow', 'Cabrio', 1.7),
    Car('Citroen', 'C5', 2, 2016, 'green', 'SUV', 1.5),
    Car('BMW ', 'Seria 1', 4, 2010, 'green', 'Coupe', 2.6)
]
Car.print_welcome_message()

for years in range(len(cars)):
    if cars[years].is_to_old() == True:
        print(cars[years])

print(cars[1].car_description())

for models in range(len(cars)):
    if cars[models].motor_option('Hatchback') == True:
        print(cars[models])
    

