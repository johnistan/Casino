class Outcome(object):
    """Holds the outcome of all potential bets within a game """

    def __init__(self, name, odds):
        """initalizer for the Outcome Class

        :name: str
        :odds: (int) the odds of winning the outcome. Assumes a denominator of 1 e.g.( 2:1 odd would be represented as 2)

        """
        self._name = name
        self._odds = odds

    @property
    def name(self):
        return self._name

    @property
    def odds(self):
        return self._odds

    def winAmount(self, amount):
        """Calculates the amount won for any given amount

        :amount: amount of bet
        :returns: amount won

        """
        return amount * self._odds

    def __str__(self):
        return '{0} with odds: {1}:1'.format(self._name, self._odds)

    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._name)

