from outcome import Outcome

def test():
    assert True

def test_outcome_init():
    black = Outcome("Black",1)

    assert black.name == "Black"
    assert black.odds == 1

def test_outcome_str():
    black = Outcome("Black",10)
    assert str(black) == "Black with odds: 10:1"

def test_outcome_winAmount():
    black = Outcome("Black",10)
    assert black.winAmount(5) == 50


def test_outcome_eq():
    red = Outcome("Red",1)
    red_dup = Outcome("Red",1)
    assert red == red_dup

    not_red = Outcome("Red1",2)
    assert red != not_red

    diff_red = Outcome("Red",2)
    assert red == diff_red


def test_outcome_hash():
    red = Outcome("Red",1)
    red_dup = Outcome("Red",1)
    assert hash(red) == hash(red_dup)
