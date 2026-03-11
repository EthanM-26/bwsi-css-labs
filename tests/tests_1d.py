import pytest
from labs.lab_1.lab_1d import two_sum

def test_positive_and_negative():
    assert two_sum([-2, 7, -11, 15], -4) == [1,2]

def test_all_positive():
    assert two_sum([78, 4, 1, 6], 7) == [2,3]

def test_all_negative():
    assert two_sum([-1, -2, -3], -4) == [0,2]

def test_zeroes_included():
    assert two_sum([0, -3, 5, -2, 1], 5) == [0,2]

def test_duplicates():
    assert two_sum([3,3], 6) == [0,1]