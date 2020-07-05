class Car():

    def __init__(self, fuel_tank, color, max_speed, wheels=4, steering_wheel=1):
        self.wheels = wheels
        self.steering_wheel = steering_wheel
        self.fuel_tank = fuel_tank
        self.color = color
        self.max_speed = max_speed

    def run(self, seconds):
        for second in range(0, seconds + 1):
            if(self.fuel_tank != 0):
                print("vroom vroom")
                self.fuel_tank -= 1
            else:
                print("Out of fuel")
    
    def back_up(self):
        print("beep beep")

class Dacia(Car):
    def __init__(self, fuel_tank, color, max_speed, cc, brand, traction, wheels=4, steering_wheel=1):
        super().__init__(fuel_tank, color, max_speed, wheels, steering_wheel)
        self.cc = cc
        self.brand = brand
        self.traction = traction
    
    def can_it_go(self):
        if(self.traction == "4x4" and self.cc > 200):
            print("I'm going!")
        else:
            print("I'm stuck!")

    def return_brand(self):
        print(self.brand)

    def return_color(self):
        print(self.color)

Car_1 = Car(5, "red", 200)
Car_1.run(5)

Car_2 = Dacia(20, "yellow", 250, 300, "Logan", "4x4")
Car_2.can_it_go()

Car_3 = Dacia(20, "blue", 130, 300, "MCV", "4x4")
Car_3.return_brand()

Car_4 = Dacia(20, "red", 250, 199, "Logan", "4x4")
Car_4.can_it_go()

Car_5 = Dacia(20, "black", 250, 110, "Logan", "4x4")
Car_5.return_color()
