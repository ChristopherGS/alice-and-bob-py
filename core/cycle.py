import random

def simulate(setback_percent, people):
    for person in people:
        if random.random() <= person.setback_rate:
            person.cash *= 1 - setback_percent
        else:
            person.cash *= 1 + person.growth_rate
