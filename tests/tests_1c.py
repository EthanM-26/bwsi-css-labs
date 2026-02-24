import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_positive_and_negative():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_all_positive():
    assert max_subarray_sum([1,2,3,4]) == 10

def test_all_negative():
    assert max_subarray_sum([-1,-2,-3]) == -1

def test_single_element():
    assert max_subarray_sum([5]) == 5

def test_zeroes_included():
    assert max_subarray_sum([0, -3, 5, -2, 1]) == 5

def test_empty_list():
    with pytest.raises(ValueError, match="Input list must not be empty"):
        max_subarray_sum([])

def test_invalid_input():
    with pytest.raises(TypeError, match="Invalid input. Please enter valid numbers."):
        max_subarray_sum([1,"w",3,"e"])