import pytest
import random
from random_number import append_random_numbers

def test_append_random_numbers():

    numbers_list = [1, 2]
    append_random_numbers(numbers_list)
    assert len(numbers_list) == 3
    append_random_numbers(numbers_list, quantity=2)
    assert len(numbers_list) == 5

pytest.main(["-v", "--tb=line", "-rN", __file__])

