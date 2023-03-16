"""factory.py : Factory class for creating objects.
"""

class Vehicle(object):
    """Vehicle class"""
    def __init__(self, wheels, capacity):
        self.wheels = wheels
        self.capacity = capacity
    
class Car(Vehicle):
    """Car class"""
    def __init__(self):
        super().__init__(4, 5)
        
class Motocycle(Vehicle):
    """Motocycle class"""
    def __init__(self):
        super().__init__(2, 2)
        
class VehicleFactory(object):
    """VehicleFactory class"""
    def create_vehicle(self, vehicle_type):
        """create_vehicle method"""
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'motocycle':
            return Motocycle()
        else:
            raise ValueError("Vehicle type not supported")
        
if __name__ == '__main__':
    factory = VehicleFactory()
    car = factory.create_vehicle('car')
    motorcycle = factory.create_vehicle('motorcycle')
        