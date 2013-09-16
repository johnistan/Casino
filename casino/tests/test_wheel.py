from wheel import Wheel
from outcome import Outcome
from bin import Bin

import random


class NonRandomNumberGenerator(random.Random):
    """ Non random generator that always return the first element """
    def choice(self, population):
        """@todo: Docstring for sample

        :population: @todo
        :returns: @todo

        """
        if population:
            return population[0]
        else:
            return []

def test_wheel_init():
    wheel = Wheel(NonRandomNumberGenerator())
    assert len(wheel.bins) == 38

def test_wheel_add():
    outcome = Outcome("00", 35)
    wheel = Wheel(NonRandomNumberGenerator())
    wheel.addOutcome(0, outcome)
    assert outcome in wheel.bins[0]

def test_wheel_next():
    outcome = Outcome("00", 35)
    wheel = Wheel(NonRandomNumberGenerator())
    wheel.addOutcome(0, outcome)
    # Non random will return first
    assert outcome in wheel.next()

    outcome = Outcome("00", 35)
    wheel = Wheel(NonRandomNumberGenerator())
    wheel.addOutcome(1, outcome)
    # Non random will return first
    assert outcome not in wheel.next()

    random_wheel = Wheel()
    for i in range(38):
        random_wheel.addOutcome(i, outcome)

    assert outcome in random_wheel.next()
