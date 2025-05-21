from abc import ABC, abstractmethod
from datetime import datetime


class Ride_sharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __str__(self):
        return f"Company name: {self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}"


class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        pass


class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.wallet = initial_amount
        self.current_ride = None
        self.current_location = current_location

    def display_profile(self):
        print(
            f"Rider: {self.name}, Email: {self.email}, Wallet: {self.wallet}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
            print(f"Amount loaded. Current balance: {self.wallet}")
        else:
            print("Invalid amount.")

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = Ride_request(self, destination)
        ride_matching = Ride_matching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        if ride:
            ride.rider = self
            self.current_ride = ride
            ride_sharing.rides.append(ride)
            print("YAY!!! We got a ride")
        else:
            print("No ride found")

    def show_current_ride(self):
        print(self.current_ride if self.current_ride else "No ride in progress")


class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location

    def display_profile(self):
        print(
            f"Driver: {self.name}, Email: {self.email}, Wallet: {self.wallet}")

    def accept_ride(self, ride):
        ride.start_ride()
        ride.set_driver(self)

    def reach_destination(self, ride):
        ride.end_ride()


class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)
        self.vehicle = vehicle

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        print(f"Ride complete. Fare: {self.estimated_fare}")
        print(f"{self.rider.name}'s wallet: {self.rider.wallet}")
        print(f"{self.driver.name}'s wallet: {self.driver.wallet}")
        self.rider.current_ride = None

    def calculate_fare(self, vehicle):
        distance = 10
        fare_per_km = {
            'car': 30,
            'bike': 20,
            'cng': 25
        }
        return distance * fare_per_km.get(vehicle)

    def __repr__(self):
        return f"Ride: {self.start_location} ➝ {self.end_location}, Vehicle: {self.vehicle.vehicle_type}"


class Ride_request:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class Ride_matching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_driver(self, ride_request, vehicle_type):
        for driver in self.available_drivers:
            if vehicle_type == 'car':
                vehicle = Car('car', '12BCC45', 30)
            elif vehicle_type == 'bike':
                vehicle = Bike('bike', 'BK123B', 50)
            elif vehicle_type == 'cng':
                vehicle = Cng('cng', 'CNG5566', 40)
            else:
                return None
            ride = Ride(ride_request.rider.current_location,
                        ride_request.end_location, vehicle)
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
        pass


class Bike(Vehicle):
    def start_drive(self):
        pass


class Cng(Vehicle):
    def start_drive(self):
        pass


# ----------------- MENU SYSTEM ----------------- #

def main():
    ride_sharing = Ride_sharing("Pathao Ride")
    riders = {}
    drivers = {}

    while True:
        print("\n========== Ride Sharing Menu ==========")
        print("1. Add Rider")
        print("2. Add Driver")
        print("3. Load Cash to Rider Wallet")
        print("4. Request a Ride")
        print("5. Show Current Ride")
        print("6. Complete Ride")
        print("7. Show Profiles")
        print("8. Exit")
        print("=======================================\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Rider Name: ")
            email = input("Enter Email: ")
            nid = input("Enter NID: ")
            location = input("Enter Current Location: ")
            amount = int(input("Initial Wallet Amount: "))
            rider = Rider(name, email, nid, location, amount)
            riders[name] = rider
            ride_sharing.add_rider(rider)
            print("Rider added.")

        elif choice == '2':
            name = input("Enter Driver Name: ")
            email = input("Enter Email: ")
            nid = input("Enter NID: ")
            location = input("Enter Current Location: ")
            driver = Driver(name, email, nid, location)
            drivers[name] = driver
            ride_sharing.add_driver(driver)
            print("Driver added.")

        elif choice == '3':
            name = input("Enter Rider Name: ")
            amount = int(input("Enter Amount to Load: "))
            if name in riders:
                riders[name].load_cash(amount)
            else:
                print("Rider not found.")

        elif choice == '4':
            name = input("Enter Rider Name: ")
            if name in riders:
                destination = input("Enter Destination: ")
                vehicle_type = input(
                    "Enter Vehicle Type (car/bike/cng): ").lower()
                riders[name].request_ride(
                    ride_sharing, destination, vehicle_type)
            else:
                print("Rider not found.")

        elif choice == '5':
            name = input("Enter Rider Name: ")
            if name in riders:
                riders[name].show_current_ride()
            else:
                print("Rider not found.")

        elif choice == '6':
            name = input("Enter Driver Name: ")
            if name in drivers:
                for rider in ride_sharing.riders:
                    if rider.current_ride and rider.current_ride.driver.name == name:
                        drivers[name].reach_destination(rider.current_ride)
                        break
                else:
                    print("No active ride found for this driver.")
            else:
                print("Driver not found.")

        elif choice == '7':
            print("\n--- Riders ---")
            for r in riders.values():
                r.display_profile()
            print("\n--- Drivers ---")
            for d in drivers.values():
                d.display_profile()

        elif choice == '8':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
