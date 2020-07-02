class Employee():

    raise_amount = 1.05

    def __init__(self, first_name, last_name, age, gender, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.pay = pay

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

class Developer(Employee):

    def __init__(self, first_name, last_name, age, gender, pay, specialty, certifications, experience):
        super().__init__(first_name, last_name, age, gender, pay)
        self.specialty = specialty
        self.certifications = certifications
        self.experience = experience

    def get_details(self):
        return f'{self.get_full_name()} is a {self.specialty} developer, aged {self.age}, with {self.experience} years of experience'

    def apply_raise(self):
        if self.experience >= 2:
            self.raise_amount = 1.1
        self.pay = self.pay * self.raise_amount




employee1 = Employee('Jerome', 'Brown', 35, 'male', 1200)

employee1.apply_raise()
print(f'Successfully applied a raise of {employee1.raise_amount} for {employee1.get_full_name()}. Pay is now {employee1.pay:.0f}')


developer1 = Developer('Chuck', 'Griffin', 29, 'male', 1000, 'Python', None, 1)
developer2 = Developer('Tina', 'Wilson', 32, 'female', 1500, 'Java', 'Bachelor\'s Degree', 3)

print(developer1.get_details())
developer1.apply_raise()
print(f'Successfully applied a raise of {developer1.raise_amount} for {developer1.get_full_name()}. Pay is now {developer1.pay:.0f}')

print(developer2.get_details())
developer2.apply_raise()
print(f'Successfully applied a raise of {developer2.raise_amount} for {developer2.get_full_name()}. Pay is now {developer2.pay:.0f}')
