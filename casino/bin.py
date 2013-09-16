
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


    def __iter__(self):
        return iter(self._outcomes)


