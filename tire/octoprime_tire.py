import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from tire.tire import Tire

class Octoprime(Tire):
    def __init__(self, list: list):
        self.list=list

    def needs_service(self):
        sum =0
        for value in self.list:
            sum += value
            if sum >= 3:
                return True
        return False