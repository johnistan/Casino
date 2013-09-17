from bin import Bin
import random

class Wheel(object):
    """Docstring for Wheel """
    _outcomeLookup = {}

    def __init__(self, rng = None):
        """@todo: to be defined

        :rng: Random Number Generator

        """
        if rng:
            self._rng = rng
        else:
            self._rng = random.Random()
        self._bins = [Bin() for i in range(38)]

    @property
    def bins(self):
        return self._bins

    @property
    def outcomeLookup(self):
        #if not self._outcomeMapping:
            #self._outcomeMapping = {o.name:o for o in self.allOutcomes}

        return self._outcomeLookup

    def getOutcome(self, name):
        """Looks up outcome by name from the mapping built by BinBuilder

        :name: str name ot outcome to lookup
        :returns: @todo

        """
        return self._outcomeLookup[name]

    def addOutcome(self, index, outcome):
        """Used to replace or add an outcome to a specific outcome

        :index: int of the bin location
        :outcome: the Outcome to store within the bin

        """
        #Build Mapping
        self._outcomeLookup[outcome.name] = outcome
        self._bins[index].add(outcome)

    def get(self, index):
        """returns the bin at any given index

        :index: int between 0 and 37 inclusive
        :returns: Bin

        """
        return self._bins[index]

    def next(self):
        """returns a rundom bin using rng.sample
        :returns: Bin

        """
        bin =  self._rng.choice(self._bins)
        return bin


