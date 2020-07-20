class Car:
    def __init__(self):  # Constructor
        self.__length = 100  # Private attribute '__' annotation
        self.__width = 30
        self.__wheels = 4
        self.__on_movement = False
        self.__gas = None
        self.__oil = None
        self.__closed_doors = True

    def start(self):  # Method
        if self.__check() and not self.__on_movement:
            self.__on_movement = True
            return self.__state()
        else:
            return "Error starting"

    def stop(self):
        self.__on_movement = False
        return self.__state()

    def __state(self):  # Private method
        if self.__on_movement:
            return "Moving"
        else:
            return "Stopped"

    def __check(self):
        print("Checking...")
        self.__gas = "Ready"
        self.__oil = "Ready"
        return self.__gas == "Ready" and self.__oil == "Ready" and self.__closed_doors


myCar = Car()
print(myCar.start())
print(myCar.stop())
print("---------------------- Another car ----------------------")
myCar_2 = Car()
print(myCar_2.start())
