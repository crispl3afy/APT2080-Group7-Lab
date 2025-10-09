import pytest
from data_processor import calculate_average

def test_calculate_average_normal_case():
    result = calculate_average([10, 20, 30])
    assert result == 20.0

def test_calculate_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])

def test_calculate_average_invalid_input():
    with pytest.raises(ValueError):
        calculate_average([10, "x", 30])

def test_calculate_average_negative_numbers():
    result = calculate_average([-10, -20, -30])
    assert result == -20.0
