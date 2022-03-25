import pytest


def always_returns_true():
    return True

def heathers_function(test_data):
    return not test_data

def test_always_returns_true():
    assert always_returns_true()

def jae_function():
    return True 

def test_heathers_function():
    test_data = False
    test_return = heathers_function(test_data)
    assert test_return == True