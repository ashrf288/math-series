from math_series import __version__
from math_series.series import fibonacci

def test_version():
    assert __version__ == '0.1.0'


def test_version():
    #input
    n=1
    assert fibonacci(n) == n