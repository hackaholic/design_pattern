
from abc import ABC, abstractmethod

# Computer Factory

class CPU(ABC):
    @abstractmethod
    def create_cpu(self):
        pass

class RAM(ABC):
    @abstractmethod
    def create_ram(self):
        pass

class Storage(ABC):
    @abstractmethod
    def create_storage(self):
        pass


class IntelCPU(CPU):
    def create_cpu(self):
        return "Intel CPU created"

class AMDCPU(CPU):
    def create_cpu(self):
        return "AMD CPU created"

class DDR4RAM(RAM):
    def create_ram(self):
        return "DDR4 RAM created"

class DDR5RAM(RAM):
    def create_ram(self):
        return "DDR5 RAM created"

class SSDStorage(Storage):
    def create_storage(self):
        return "SSD Storage created"

class HDDStorage(Storage):
    def create_storage(self):
        return "HDD Storage created"

# Abstract Factory
class ComputerFactory(ABC):
    def __init__(self):
        self._register = {}

    # pyhton 3.10+ or newer support multiple return type hint
    # def register_hardware(self, hardware_type: str, hardware: CPU|RAM|Storage):
    def register_hardware(self, hardware_type: str, hardware: object): 
        self._register[hardware_type] = hardware

    # def create_component(self, component_type: str) -> CPU|RAM|Storage):
    def create_component(self, component_type: str) -> object:
        if component_type not in self._register:
            raise ValueError(f"{component_type.upper()} not registered!")
        return self._register[component_type]()


    @abstractmethod
    def create_cpu(self) -> CPU:
        pass

    @abstractmethod
    def create_ram(self) -> RAM:
        pass

    @abstractmethod
    def create_storage(self) -> Storage:
        pass

# Concrete Factories
class LaptopFactory(ComputerFactory):
    def __init__(self):
        super().__init__()

    def create_cpu(self) -> CPU:
       return self.create_component("cpu")

    def create_ram(self) -> RAM:
        return self.create_component("ram")

    def create_storage(self) -> Storage:
        return self.create_component("storage")

class DesktopFactory(ComputerFactory):
    def __init__(self):
        super().__init__()

    def create_cpu(self) -> CPU:
       return self.create_component("cpu")

    def create_ram(self) -> RAM:
        return self.create_component("ram")

    def create_storage(self) -> Storage:
        return self.create_component("storage")

def assemble_computer(factory: ComputerFactory):
    cpu = factory.create_cpu()
    ram = factory.create_ram()
    storage = factory.create_storage()

    print(cpu.create_cpu())
    print(ram.create_ram())
    print(storage.create_storage())




laptop = LaptopFactory()
laptop.register_hardware("cpu", IntelCPU)
laptop.register_hardware("ram", DDR5RAM)
laptop.register_hardware("storage", SSDStorage)

desktop = DesktopFactory()
desktop.register_hardware("cpu", AMDCPU)
desktop.register_hardware("ram", DDR4RAM)
desktop.register_hardware("storage", HDDStorage)

# Assembling Computers
print("Laptop Configuration:")
assemble_computer(laptop)

print("\nDesktop Configuration:")
assemble_computer(desktop)

