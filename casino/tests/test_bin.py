from bin import Bin
from outcome import Outcome

def test_bin_init():
    bin = Bin( Outcome("00", 35), Outcome("0", 35))
    assert len(bin.outcomes) == 2

def test_bin_add():
    outcome = Outcome("00", 35)
    bin = Bin( outcome)
    assert len(bin.outcomes) == 1

    #Sets are unique by hash and eq
    bin.add( Outcome("00", 35) )
    assert len(bin.outcomes) == 1

    bin.add( Outcome("0", 35) )
    assert len(bin.outcomes) == 2

def test_bin_reference():
    outcome = Outcome("00", 35)
    bin = Bin(outcome)
    bin2 = Bin(outcome)
    assert next(iter(bin.outcomes)) == next(iter(bin2.outcomes))
    assert id(next(iter(bin.outcomes))) == id(next(iter(bin2.outcomes)))

def test_bin_in():
    bin = Bin( Outcome("00", 35), Outcome("0", 35))
    outcome = Outcome("00", 35)

    assert outcome in bin

def test_bin_str():
    outcome = Outcome("00", 35)
    outcome2 = Outcome("0", 35)
    bin = Bin(outcome, outcome2)
    assert str(bin) == "0 with odds: 35:1, 00 with odds: 35:1"
