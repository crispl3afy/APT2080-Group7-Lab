import pytest
from data_processor import calculate_average


def test_average_with_positive_numbers():
    """Test average calculation with positive numbers."""
    result = calculate_average([10, 20, 30])
    assert result == 20.0


def test_average_with_negative_numbers():
    """Test average calculation with negative numbers."""
    result = calculate_average([-10, -20, -30])~~~~~~~~~~~~~~~
    assert result == -20.0


def test_average_with_mixed_numbers():
    """Test average with both positive and ~~negative numbers."""
    result = calculate_average([-10, 0, 10])
    assert result == 0.0


def test_average_with_single_number():
    """Test average with a single-element list."""
    result = calculate_average([5])
    assert result == 5.0


def test_average_with_empty_list():
    """Test that ValueError is raised for an empty list."""
    with pytest.raises(ValueError):
        calculate_average([])