import pytest
from guessnumbers import guessnumber

def test_easy():

    testnumber = guessnumber()
    number = testnumber.easy()
    assert number <= 10
    assert number >= 1

def test_medium():
    
    testnumber = guessnumber()
    number = testnumber.medium()
    assert number <= 100
    assert number >= 1

def test_hard():

    testnumber = guessnumber()
    number = testnumber.hard()
    assert number <= 1000
    assert number >= 1
    
pytest.main(["-v", "--tb=line", "-rN", __file__])