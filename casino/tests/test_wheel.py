from wheel import Wheel
from outcome import Outcome
from bin import Bin
from bin import BinBuilder
from roulette import RouletteGame

import random
import pytest


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


def test_non_random():
    rng = NonRandomNumberGenerator()
    assert 99 == rng.choice([99,88,77])

def test_wheel_init():
    wheel = Wheel(NonRandomNumberGenerator())
    assert len(wheel.bins) == 38

def test_wheel_add():
    outcome = Outcome("00", 35)
    wheel = Wheel(NonRandomNumberGenerator())
    wheel.addOutcome(4, outcome)
    assert outcome in wheel.get(4)
    with pytest.raises(IndexError):
        wheel.get(40)

def test_wheel_get():
    outcome = Outcome("00", 35)
    wheel = Wheel(NonRandomNumberGenerator())
    wheel.addOutcome(4, outcome)
    assert outcome in wheel.bins[4]

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


#########################


def test_buildBins_firstColNumbers():
    assert list(BinBuilder.firstColumnNumbers())[0] == 1
    assert list(BinBuilder.firstColumnNumbers())[11] == 34

def test_buildBins_secondColNumbers():
    assert list(BinBuilder.secondColumnNumbers())[0] == 2
    assert list(BinBuilder.secondColumnNumbers())[11] == 35

def test_buildBins_firstTwoColNumbers():
    assert list(BinBuilder.firstTwoColumnNumbers())[0] == 1
    assert list(BinBuilder.firstTwoColumnNumbers())[12] == 2
    assert list(BinBuilder.firstTwoColumnNumbers())[13] == 5
    assert list(BinBuilder.firstTwoColumnNumbers())[23] == 35
    with pytest.raises(IndexError):
        list(BinBuilder.firstTwoColumnNumbers(11))[23]

def test_buildBins():
    wheel = Wheel()
    builder = BinBuilder()
    assert wheel == builder.buildBins(wheel)

def test_straightbet_builder():
    wheel = Wheel()
    builder = BinBuilder()

    number1 = Outcome("Number 1", RouletteGame.StraightBet)

    builder._buildStraightBets(wheel)
    assert number1 in wheel.get(1)
    assert Outcome("Number 0", RouletteGame.StraightBet) in wheel.get(0)
    assert Outcome("Number 00", RouletteGame.StraightBet) in wheel.get(37)

def test_splitbet_builder():
    wheel = Wheel()
    builder = BinBuilder()

    split1_2 = Outcome("Split 1-2", RouletteGame.SplitBet)
    builder._buildSplitBets(wheel)

    assert split1_2 in wheel.get(1)
    assert len(wheel.get(1)) == 2
    assert len(wheel.get(2)) == 3
    assert len(wheel.get(5)) == 4

def test_streetbet_builder():
    wheel = Wheel()
    builder = BinBuilder()

    street1_2_3 = Outcome("Street 1-2-3", RouletteGame.StreetBet)
    builder._buildStreetBets(wheel)
    assert street1_2_3 in wheel.get(1)

def test_cornerbet_builder():
    wheel = Wheel()
    builder = BinBuilder()

    corner1 = Outcome("Corner 1-2-4-5", RouletteGame.CornerBet)
    builder._buildCornerBets(wheel)
    assert corner1 in wheel.get(1)

    corner36 = Outcome("Corner 32-33-35-36", RouletteGame.CornerBet)
    assert corner36 in wheel.get(36)

def test_linebet_builder():
    wheel = Wheel()
    builder = BinBuilder()

    line1 = Outcome("Line 1-2-3-4-5-6", RouletteGame.LineBet)
    builder._buildLineBets(wheel)
    assert line1 in wheel.get(1)


def test_colbet_builder():
    wheel = Wheel()
    builder = BinBuilder()

    col1 = Outcome("Column 1", RouletteGame.ColumnBet)
    col2 = Outcome("Column 2", RouletteGame.ColumnBet)
    builder._buildColumnBets(wheel)
    assert col1 in wheel.get(1)
    assert col2 not in wheel.get(1)
    assert col2 in wheel.get(2)

def test_dozenbets_builder():
    wheel = Wheel()
    builder = BinBuilder()

    dozen1 = Outcome("Dozen 1", RouletteGame.DozenBet)
    dozen2 = Outcome("Dozen 2", RouletteGame.DozenBet)
    builder._buildDozenBets(wheel)
    assert dozen1 in wheel.get(1)
    assert dozen2 not in wheel.get(1)

def test_evenmoneybets_builder():
    wheel = Wheel()
    builder = BinBuilder()

    red = Outcome("Red", RouletteGame.EvenMoneyBet)
    black = Outcome("Black", RouletteGame.EvenMoneyBet)
    builder._buildEvenMoneyBets(wheel)
    assert red in wheel.get(1)
    assert black in wheel.get(2)

    even = Outcome("Even", RouletteGame.EvenMoneyBet)
    assert even not in wheel.get(3)
    assert even in wheel.get(2)
