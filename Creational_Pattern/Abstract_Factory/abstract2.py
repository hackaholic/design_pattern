# Car Manufacturing Factory

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def assemble(self):
        pass

class Engine(ABC):
    @abstractmethod
    def create_engine(self):
        pass


class SedanCar(Car):
    def assemble(self):
        return "Sedan Car assembled"

class SUVCar(Car):
    def assemble(self):
        return "SUV Car assembled"

class V6Engine(Engine):
    def create_engine(self):
        return "V6 Engine created"

class V8Engine(Engine):
    def create_engine(self):
        return "V8 engine created"


class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_engine(self):
        pass


class SedanFactory(CarFactory):
    def create_car(self):
        return SedanCar()
    
    def create_engine(self):
        return V6Engine()

class SUVFactory(CarFactory):
    def create_car(self):
        return SUVCar()
    
    def create_engine(self):
        return V8Engine()


def assemble_car(factory: CarFactory):
    car = factory.create_car()
    engine = factory.create_engine()
    print(engine.create_engine)
    print(car.assemble())

sedan = SedanFactory()
suv = SUVFactory()

assemble_car(sedan)
assemble_car(suv)


    

