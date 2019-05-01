from check_prime import check_prime as cp
from check_prime import PrimeNumberError
import pytest
from pytest import raises

def test_check_prime_default():
    assert cp(13) == True
    assert cp(12) == False
    assert cp(2) == True
    assert cp(57) == True

def test_check_prime_exception():
    with raises(PrimeNumberError):
        cp(-3)
    with raises(PrimeNumberError):
        cp(0)
    with raises(TypeError):
        cp(6.3)
    with raises(TypeError):
        cp(6/2)
    with raises(TypeError):
        cp("nanigasi")
    with raises(TypeError):
        cp("5")
    with raises(TypeError):
        cp([4,1,6])
    with raises(TypeError):
        cp()
