from math_series import __version__
from math_series.series import fibonacci
from math_series.series import Lucas

def test_version():
    assert __version__ == '0.1.0'


def test_version1():
    #input
    n=0
    assert fibonacci(n) == 0

def test_version2():
    #input
    n=4
    assert fibonacci(n) == 2

def test_version2():
    #input
    n=2
    assert fibonacci(n) == 1

def test_version3():
    #input
    n=10
    assert fibonacci(n) == 34
    ## lucas testing
def test_version4():
    #input
    n=10
    assert Lucas(n) == 10