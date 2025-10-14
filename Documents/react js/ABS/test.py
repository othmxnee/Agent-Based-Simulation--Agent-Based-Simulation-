from mesa import Model
from mesa.time import RandomActivation

class TestModel(Model):
    def __init__(self):
        self.schedule = RandomActivation(self)

print("Mesa is working!")
