class Vehicle:
    brand = "Honda"
    def Horn(self):
        print("Beep Beep")
class Bike(Vehicle):
    wheels = 2
    def ride(self):
        print(f"riding on{self.wheels}wheels")
