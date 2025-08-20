from example1 import is_even

def test_positive_even():
    assert is_even(2) == True
    assert is_even(10) == True

def test_positive_odd():
    assert is_even(3) == False
    assert is_even(17) == False

def test_zero():
    assert is_even(0) == True

def test_negative_numbers():
    assert is_even(-2) == True
    assert is_even(-7) == False
