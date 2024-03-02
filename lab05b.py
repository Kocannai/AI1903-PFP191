#Question 1

#1

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
car = Vehicle(240,18)
print(car.max_speed, car.mileage)


#2

class Vehicle:
    pass

car = Vehicle()

#Question 2

#1

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

bus = Bus('School Volvo', 180, 12)
print('Vehicle name:',bus.name, 'Speed:',bus.max_speed, 'Mileage:',bus.mileage)


#2

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        return f'The seating capacity of a {self.name} is {capacity} passengers'
    
class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)
    
bus = Bus('School Volvo', 180, 12)
print(bus.seating_capacity())
    
#Question 3

#1

class Vehicle:
    color = 'White'
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
     
bus = Bus('School Volve', 180, 12)
car = Car('Audi Q5', 240, 18)

print(bus.color,bus.name, 'Speed:',bus.max_speed, 'Mileage:',bus.mileage)
print(car.color,car.name, 'Speed:',car.max_speed, 'Mileage:',car.mileage)

#2

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
        
    def fare(self):
        return self.capacity * 100 + (self.capacity * 100)*(1/10)
        
class Bus(Vehicle):
    pass

bus = Bus('School Volvo', 12, 50)
print('Total Bus fare is:', bus.fare())

#Question 4

#1

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
        
class Bus(Vehicle):
    pass

bus = Bus('School Volvo', 12, 50)
print(type(bus))

#2

print(isinstance(bus,Vehicle))



















