class Vehicle:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        self.__moving = False
        self.__speed_up = False
        self.__stop = False

    def start(self):
        self.__moving = True

    def speed_up(self):
        self.__speed_up = True

    def stop(self):
        self.__stop = True

    def __str__(self):  # toString() like method
        return f"Brand:\t\t\t{self.__brand}\nModel:\t\t\t{self.__model}\nMoving:\t\t\t{self.__moving}\nSpeed up:\t\t{self.__speed_up}\nStop:\t\t\t{self.__stop}"


class Motorcycle(Vehicle):  # Motorcycle inherit attributes and methods of Vehicle class:

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.__one_wheel = "Nope"

    def one_wheel(self):
        self.__one_wheel = "On one wheel!"

    def __str__(self):  # Overriding method from Vehicle class
        super_str = super(Motorcycle, self).__str__()  # Way to call class str method of super class
        return "{}\nPower wheelie:\t{}".format(super_str, self.__one_wheel)


class Truck(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.__load = []

    def load(self, stuffs):
        self.__load.append(stuffs)

    def load_state(self):
        if len(self.__load) > 0:
            return f"Loaded with {len(self.__load)} stuff(s)"
        else:
            return "No loaded"


class ElectricVehicle:

    def __init__(self):
        self.__autonomy = 100
        self.__charging = False

    def charge(self):
        self.__charging = True

    def __str__(self):
        return f"Autonomy:\t\t{self.__autonomy}\nCharging:\t\t{self.__charging}"


# If a class has multiple heritage, priority order is from left to right. This is appreciable
# when the constructor method (__init__) is called
class ElectricBike(Vehicle, ElectricVehicle):

    def __init__(self, brand, model):
        super(ElectricBike, self).__init__(brand, model)

    # TODO Resolve how to call super classes methods when an object has multiple heritage
    def __str__(self):
        vehicle_str = super(ElectricBike, self).__str__()
        print(super(ElectricBike, self))
        electric_vehicle_str = super(ElectricVehicle, self).__str__()
        return f"{vehicle_str}\n{electric_vehicle_str}"


print("-------------------- Motorcycle --------------------")
my_motorcycle = Motorcycle("Honda", "CBR")
my_motorcycle.one_wheel()
print(my_motorcycle)

print("-------------------- Truck --------------------")
my_truck = Truck("Mercedez", "Z10E")
print(my_truck.load_state())
my_truck.load("Rocks")
print(my_truck.load_state())

print("-------------------- Electric bike --------------------")
my_electric_bike = ElectricBike("Jeep", "P3R")
my_electric_bike.charge()
my_electric_bike.__setattr__("__autonomy", 50)
print(my_electric_bike.__getattribute__("__autonomy"))
print(my_electric_bike)
