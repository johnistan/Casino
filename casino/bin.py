from roulette import RouletteGame
from outcome import Outcome
import itertools

class Bin(object):
    """A holder of outcomes that will make up a wheel"""

    def __init__(self, *outcomes):
        """Will accept a varible number of Outcomes to hold

        :outcome: a series of Outcomes

        """
        self._outcomes= frozenset(outcomes)

    @property
    def outcomes(self):
        return self._outcomes

    def add(self, *outcome):
        """Used to add new Outcomes to the bin

        :outcome: @todo
        :returns: @todo

        """
        self._outcomes |= set(outcome)

    def __str__(self):
        if self._outcomes:
            return ', '.join(map(str, self._outcomes))
        else:
            return "[]"
    def __repr__(self):
        return "<Bin of outcomes: {0}>".format(str(self))
    def __len__(self):
        return len(self._outcomes)


    def __iter__(self):
        return iter(self._outcomes)





class BinBuilder(object):
    """Used to build the outcome within a wheel"""
    def __init__(self):
        pass

    def buildBins(self, wheel):
        """Static Method to initalize bin on a wheel with outcomes

        :wheel: wheel
        :returns: wheel

        """
        self._wheel = wheel

        self._buildStraightBets(wheel)

        return self._wheel

    @staticmethod
    def firstColumnNumbers(n=12):
        """Returns all numbers in the first rowi
        defaults to all number. can restrict by passing an optional n arg
        """
        for i in range(n):
            yield i*3+1

    @staticmethod
    def secondColumnNumbers(n=12):
        for i in range(n):
            yield i*3+2

    @staticmethod
    def firstTwoColumnNumbers(n = 12):
        return itertools.chain(BinBuilder.firstColumnNumbers(n), BinBuilder.secondColumnNumbers(n))

    def _buildStraightBets(self, wheel):
        """build straight bets. One for each number including 0 and 00
        :wheel: Wheel
        :returns: @todo

        """
        for i in range(36):
            wheel.addOutcome(i, Outcome("Number {0}".format(i), RouletteGame.StraightBet))

        wheel.addOutcome(37, Outcome("Number 00", RouletteGame.StraightBet))

    def _buildSplitBets(self, wheel):
        """Build split bets by looping the numbers and calculating (n, n+1) for left-right splits and (n,n+3) splits

        :wheel: Wheel
        """
        for i in BinBuilder.firstTwoColumnNumbers():
            outcome = Outcome("Split {0}-{1}".format(i, i + 1), RouletteGame.SplitBet)
            wheel.addOutcome(i , outcome)
            wheel.addOutcome(i + 1, outcome)

        #up-down splits
        for i in range(34):
            down_number = i + 3
            up_down_outcome = Outcome("Split {0}-{1}".format(i, down_number), RouletteGame.SplitBet)
            wheel.addOutcome(i, up_down_outcome)
            wheel.addOutcome(down_number, up_down_outcome)

    def _buildStreetBets(self, wheel):
        """Build a street bet for every row

        :wheel: Wheel

        """
        for first_col_number in BinBuilder.firstColumnNumbers():
            outcome = Outcome("Street {0}-{1}-{2}".format(*[first_col_number + x for x in [0,1,2]])
                                                , RouletteGame.StreetBet)
            for n in range(first_col_number, first_col_number +3):
                wheel.addOutcome(n, outcome)

    def _buildCornerBets(self, wheel):
        """@todo: Docstring for _build

        :wheel: Wheel

        """
        for i in BinBuilder.firstTwoColumnNumbers(11):
            outcome = Outcome("Corner {0}-{1}-{2}-{3}".format(*[i + x for x in [0, 1, 3, 4]]), RouletteGame.CornerBet)
            print outcome
            [wheel.addOutcome(i+x,outcome) for x in [0, 1, 3, 4]]

    def _buildLineBets(self, wheel):
        """Fill the bins with the outcomes for line bets

        :wheel: @todo
        :returns: @todo

        """
        for i in BinBuilder.firstColumnNumbers(11):
            outcome = Outcome("Line {0}-{1}-{2}-{3}-{4}-{5}".format(*[i + x for x in [0,1,2,3,4,5]]), RouletteGame.LineBet)
            [wheel.addOutcome(i+x,outcome) for x in [0,1,2,3,4,5]]

    def _buildColumnBets(self, wheel):
        """Add column bet outcomes to bins

        :wheel: @todo
        :returns: @todo

        """
        for c in range(1,4):
            outcome = Outcome("Column {0}".format(c), RouletteGame.ColumnBet)
            for i in range(0,12):
                wheel.addOutcome(i*3 + c , outcome)

    def _buildDozenBets(self, wheel):
        """all dozen outcomes

        :wheel: @todo
        :returns: @todo

        """
        for d in range(0,3):
            outcome = Outcome("Dozen {0}".format(d + 1), RouletteGame.DozenBet)
            for i in range(0,11):
                wheel.addOutcome(12 * d + i, outcome)

