import pytest


def always_returns_true():
    return True

def heathers_function(test_data):
    return not test_data

def test_always_returns_true():
    assert always_returns_true()
