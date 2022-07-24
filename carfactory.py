from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindlerbattery import SpindlerBattery
from battery.nubbinbattery import NubbinBattery

class CarFactory():

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_milage: int, last_service_milage: int):
        engine = CapuletEngine(last_service_milage, current_milage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
#a
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_milage: int, last_service_milage: int):
        engine = WilloughbyEngine(last_service_milage, current_milage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_milage: int, last_service_milage: int):
        engine = WilloughbyEngine(last_service_milage, current_milage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_milage: int, last_service_milage: int):
        engine = CapuletEngine(last_service_milage, current_milage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car