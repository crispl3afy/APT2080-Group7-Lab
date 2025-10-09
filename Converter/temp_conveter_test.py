import pytest
# Import the conversion functions from the temp_converter module
from temp_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

#Ensures the conversion functions work correctly
def test_celsius_to_fahrenheit():
    #Enables testing of celsius_to_fahrenheit function
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert round(celsius_to_fahrenheit(37), 2) == 98.6

# Enables testing of fahrenheit_to_celsius function
def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert round(fahrenheit_to_celsius(98.6), 2) == 37