from sinc2d import *

def test_y():
    x=1
    expec = np.sin(x) / x
    calc = sinc2d(x,0)
    assert calc == expec
