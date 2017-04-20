#Chapter 05 - If Then

#page 76 - A Simple Example

MyCar = "Audi"
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

    if car == 'audi':
        if car == MyCar:
            print(car + " = " + MyCar)
        else:
            print(car + " != " + MyCar)


WifeCar = 'honda'

if WifeCar in cars:
    print(WifeCar + " is in " + cars)
else:
    print(WifeCar + " is not in cars list")

