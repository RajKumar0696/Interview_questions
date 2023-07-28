# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


bike = Vehicle(200, 45)
print("pulser maximum speed is", bike.max_speed, "the mileage is", bike.mileage)