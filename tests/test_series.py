from math_series import __version__
from math_series.series import fibonacci
from math_series.series import Lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_version1():
    #input
    n=0
    assert fibonacci(n) == 0

def test_version2():
    #input
    n=4
    assert fibonacci(n) == 3

def test_version2():
    #input
    n=2
    assert fibonacci(n) == 1

def test_version3():
    #input
    n=10
    assert fibonacci(n) == 55


    ## lucas testing
def test_version4():
    #input
    n=0
    assert Lucas(n) == 2
def test_version4():
    #input
    n=2
    assert Lucas(n) == 3
def test_version5():
    #input
    n=4
    assert Lucas(n) == 7


    ##  sum series testing


def sum_series():
    expected = 10
    actual = sum_series(3,4,3)
    assert actual == expected
    