
class IllegalAction(Exception):
    pass

class Tires:
    def __init__(self,tires):
        self.__pressure = tires.pressure
        self.__size = tires.size
    @property
    def details(self):
        return f"pressure is {self.__pressure} and size is {self.__size}"
    def pump(self,value):
        if self.__pressure + value < 100:
            self.__pressure += value
        else:
            raise IllegalAction("Cannot put more air...!!!")
    def __str__(self):
        return f"size is {self.__size} and pressure is {self.__pressure}"

class OffroadTires:
    def __init__(self, pressure):
        self.__pressure = pressure
        self.__size = 18
    @property
    def pressure(self):
        return self.__pressure
    @property
    def size(self):
        return self.__size

class CityTires:
    def __init__(self, pressure):
        self.__pressure = pressure
        self.__size = 15
    @property
    def pressure(self):
        return self.__pressure
    @property
    def size(self):
        return self.__size

class Engine:
    def __init__(self,vin,fuel_type):
        self.__vin = vin
        self.__fuel_type = fuel_type
    @property
    def vin(self):
        return self.__vin
    @property
    def fuel_type(self):
        return self.__fuel_type
    def start(self):
        print("Vehicle Started")
    def stop(self):
        print("Vehicle Stopped")
    def get_state(self):
        print("The Engine and tires are in good condition")
    def __str__(self):
        return f"vin = {self.__vin} and fuel type is {self.__fuel_type}."
class ElectricEngine(Engine):
    def __init__(self,vin):
        fuel_type = "Electric Engine"
        super().__init__(vin,fuel_type)
class HeatEngine(Engine):
    def __init__(self,vin):
        fuel_type = "Conventional Thermal Engine"
        super().__init__(vin,fuel_type)
    
        
class Vehicle:
    def __init__(self,tires,engine):
        self.tire_det = tires.details
        self.engine_det = f"vin is {engine.vin} and type is {engine.fuel_type}"
        self.engine = engine
        self.tires = tires
    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()
    def status(self):
        self.engine.get_state()
    def __str__(self):
        return f"Tire details => {self.tire_det}\nEngine details => {self.engine_det}"

if __name__  == "__main__":        
    vehicle = Vehicle(Tires(CityTires(100)), HeatEngine("KL-12-1915"))
    vehicle.start()
    print(vehicle)
    vehicle.status()
    vehicle.stop()