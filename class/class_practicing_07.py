class Car:
    def turn_on(self):
        print("you start the engine")
        return self
    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("you steps on the brakes")
        return self
    def turn_off(self):
        print("you turn of the engine")

    
car = Car()
car.turn_on().drive()
print("-----------------------")
car.brake().turn_off()

print("----------------------------")

car.turn_on().drive().brake().turn_off()