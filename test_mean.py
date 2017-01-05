
from mean import *

def test_ints():
    input = [1, 2, 3, 4, 5]
    calculated_value = mean(input)
    expected_value = 3
    assert calculated_value == expected_value

def test_ints2():
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    calculated_value = mean(input)
    expected_value = 5
    assert calculated_value == expected_value

