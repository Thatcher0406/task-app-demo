# Define the Vehicle class
class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

# Define the Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, registration_number, make, model, seats):
        super().__init__(registration_number, make, model)
        self.seats = seats

# Define the Truck class inheriting from Vehicle
class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

# Define the Motorcycle class inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

# Define the Fleet class
class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            print("List of Vehicles:")
            for idx, vehicle in enumerate(self.vehicles, start=1):
                print(f"Vehicle {idx}: {vehicle.make} {vehicle.model} ({vehicle.registration_number})")

    def search_vehicle(self, reg_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == reg_number:
                print(f"Vehicle found:")
                print(f"Registration Number: {vehicle.registration_number}")
                print(f"Make: {vehicle.make}")
                print(f"Model: {vehicle.model}")
                if isinstance(vehicle, Car):
                    print(f"Seats: {vehicle.seats}")
                elif isinstance(vehicle, Truck):
                    print(f"Cargo Capacity: {vehicle.cargo_capacity}")
                elif isinstance(vehicle, Motorcycle):
                    print(f"Engine Capacity: {vehicle.engine_capacity}")
                return
        print("Vehicle not found.")

# Demo of functionalities
if __name__ == "__main__":
    fleet = Fleet()

    # Adding vehicles
    car1 = Car("ABC123", "Toyota", "Camry", 5)
    truck1 = Truck("XYZ789", "Ford", "F-150", "5000 lbs")
    motorcycle1 = Motorcycle("DEF456", "Honda", "CBR600RR", "600 cc")

    fleet.add_vehicle(car1)
    fleet.add_vehicle(truck1)
    fleet.add_vehicle(motorcycle1)

    # Display all vehicles
    fleet.display_vehicles()

    # Search for a vehicle
    fleet.search_vehicle("XYZ789")
