from fib import *

def test_fib_3():
    fib3_expected = 1 + 1 + 2 + 3
    fib3_calculated = fib(3)
    assert fib3_calculated == fib3_expected
