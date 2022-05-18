class Car:
    color = None


class motorcycle:
    color = None


def change_color(Car, color):
    Car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = motorcycle()

change_color(car_1, 'red')
change_color(car_2, 'white')
change_color(car_3, 'blue')
change_color(bike_1, 'dark')


print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)