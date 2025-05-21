from datetime import datetime
from vehicle import*

class Ride:
    def __init__(self,start_location,end_location,vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)
        self.vehicle = vehicle

    def set_driver(self,driver):
        self.driver = driver
    def start_ride(self):
        self.start_time = datetime.now()
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
    def calculate_fare(self,vehicle):
        print(vehicle)
        distance = 10
        fare_per_km = {
            'car': 30,
            'bike' : 20,
            'cng' : 25
        }
        return distance * fare_per_km.get(vehicle)
    def __repr__(self):
        return f"Ride details, started {self.start_location} to {self.end_location}"

class Ride_request:
    def __init__(self,rider,end_location):
        self.rider = rider
        self.end_location = end_location

class Ride_matching:
    def __init__(self,drivers):
        self.available_drivers = drivers

    def find_driver(self,ride_request,vehicle_type):
        if len(self.available_drivers) > 0:
            print("Looking for drivers.....")
            driver = self.available_drivers[0]
            if vehicle_type == 'car':
                vehicle = Car('car','12BCC45',30)
            elif vehicle_type == 'bike':
                vehicle = Bike('bike','BK123B',50)
            ride = Ride(ride_request.rider.current_location,ride_request.end_location,vehicle)
            driver.accept_ride(ride)
            return ride