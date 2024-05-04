import random

class Person:
    def __init__(self, name):
        self.name = name
        self.cash = 100
        if name == "Alice":
            self.growth_rate = 0.10
            self.setback_rate = 0.05
            self.lie_discovered_rate = 0.05
            self.subs_growth = 100
        elif name == "Bob":
            self.growth_rate = 0.08
            self.setback_rate = 0.01
            self.lie_discovered_rate = 0.00
            self.subs_growth = 50
        else:
            raise ValueError("Unknown person")

    def __str__(self):
        return f"{self.name}: {round(self.cash, 2)}"