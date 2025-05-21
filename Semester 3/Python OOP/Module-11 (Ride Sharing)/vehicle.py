from abc import ABC, abstractmethod

class Vehicle(ABC):
    speed = {
        'car' : 50,
        'bike' : 60,
        'cng' : 20
    }
    def __init__(self,vehicle_type,license_plate,rate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)
    def start_drive(self):
        pass

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)
    def start_drive(self):
        pass