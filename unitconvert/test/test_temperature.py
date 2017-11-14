import numpy as np
import pytest

from unitconvert import temperature

def test_fahrenheit_to_celsius():
    # Test 1: Test known values
    conversion_test1 = temperature.fahrenheit_to_celsius(212)
    np.testing.assert_allclose(conversion_test1, 100, rtol = 1e-5)
        # round(1.1234,1) == 1.1

    # Test 2: Check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        temperature.fahrenheit_to_celsius(1,2)

    # Test 3: Check that 0 miles is 0 km
    assert temperature.fahrenheit_to_celsius(32) == 0

def test_celsius_to_fahrenheit():
    # Test 1: Test known values
    conversion_test1 = temperature.celsius_to_fahrenheit(100)
    np.testing.assert_allclose(conversion_test1, 212, rtol = 1e-5)

    # Test 2: Check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        temperature.celsius_to_fahrenheit(1,2)

    # Test 3: Check that 0 miles is  0 km
    assert temperature.celsius_to_fahrenheit(0) == 32
