from abc import ABC, abstractmethod
from datetime import datetime
import uuid

class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __str__(self):
        return f"{self.company_name}: {len(self.riders)} riders, {len(self.drivers)} drivers"

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
        self.user_id = str(uuid.uuid4())

    @abstractmethod
    def display_profile(self):
        pass

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.wallet = initial_amount
        self.current_location = current_location
        self.current_ride = None
        self.ride_history = []

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Invalid amount")

    def request_ride(self, app, destination, vehicle_type):
        if self.wallet < 100:
            print("Insufficient balance to request a ride.")
            return

        request = RideRequest(self, destination)
        match = RideMatching(app.drivers)
        ride = match.find_driver(request, vehicle_type)

        if ride:
            self.current_ride = ride
            ride.rider = self
            print("Ride confirmed!")
        else:
            print("No available drivers")

    def show_current_ride(self):
        print(self.current_ride or "No ongoing ride.")

    def display_profile(self):
        print(f"Rider: {self.name} | Wallet: {self.wallet}")

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.available = True
        self.ride_history = []

    def accept_ride(self, ride):
        if self.available:
            ride.set_driver(self)
            ride.start_ride()
            self.available = False

    def reach_destination(self, ride):
        ride.end_ride()
        self.available = True
        self.ride_history.append(ride)

    def display_profile(self):
        print(f"Driver: {self.name} | Wallet: {self.wallet}")

class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.ride_id = str(uuid.uuid4())
        self.start_location = start_location
        self.end_location = end_location
        self.vehicle = vehicle
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        if self.rider.wallet >= self.estimated_fare:
            self.rider.wallet -= self.estimated_fare
            self.driver.wallet += self.estimated_fare
            self.rider.ride_history.append(self)
        else:
            print("Payment failed: Insufficient funds")

    def calculate_fare(self, vehicle_type):
        distance = 10  # stubbed distance
        fare_table = {'car': 30, 'bike': 20, 'cng': 25}
        return distance * fare_table.get(vehicle_type, 0)

    def __str__(self):
        return f"Ride from {self.start_location} to {self.end_location}, Fare: {self.estimated_fare}"

class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

class RideMatching:
    def __init__(self, drivers):
        self.drivers = drivers

    def find_driver(self, request, vehicle_type):
        for driver in self.drivers:
            if driver.available:
                vehicle = None
                if vehicle_type == 'car':
                    vehicle = Car('car', 'XYZ123', 30)
                elif vehicle_type == 'bike':
                    vehicle = Bike('bike', 'BIKE123', 20)

                if vehicle:
                    ride = Ride(request.rider.current_location, request.end_location, vehicle)
                    driver.accept_ride(ride)
                    return ride
        return None

class Vehicle(ABC):
    def __init__(self, vehicle_type, license_plate, rate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate

    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def start_drive(self):
        print("Car is moving...")

class Bike(Vehicle):
    def start_drive(self):
        print("Bike is moving...")

# Sample usage
app = RideSharing("Pathao")
rifat = Rider("Rifat", "rifat@example.com", 12345, "Uttara", 1000)
sifat = Driver("Sifat", "sifat@example.com", 54321, "Abdullahpur")
app.add_rider(rifat)
app.add_driver(sifat)

rifat.request_ride(app, "Khilkhet", "car")
rifat.show_current_ride()
sifat.reach_destination(rifat.current_ride)
print(app)
