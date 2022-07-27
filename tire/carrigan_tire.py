import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from tire.tire import Tire

class Carrigan(Tire):
    def __init__(self, list: list):
        self.list = list

    def needs_service(self):
        for value in self.list:
            if value >= 0.9:
                return True
        return False


