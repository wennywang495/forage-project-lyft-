from abc import ABC, abstractmethod
from servicable import Servicable
from engine.engine import Engine
from battery.battery import Battery

class Car(Servicable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()