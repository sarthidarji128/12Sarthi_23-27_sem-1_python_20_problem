class Vehicle:
    def drive(self):
        return "Generic vehicle driving method"

class Car(Vehicle):
    def drive(self):
        return "Car is driving on the road."

class Bicycle(Vehicle):
    def drive(self):
        return "Bicycle is pedaling on the street."

vehicleObj = Vehicle()
carObj = Car()
bicycleObj = Bicycle()

print("Vehicle:")
print(vehicleObj.drive())

print("\nCar:")
print(carObj.drive())

print("\nBicycle:")
print(bicycleObj.drive())
