class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class bus(Vehicle):
    pass


Bus = bus("Sri", 100, 45)

print(Bus.name, Bus.mileage, Bus.max_speed)
