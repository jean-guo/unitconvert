import numpy as np
import pytest

from unitconvert import distance

def test_miles_to_kilometers():
    # Test 1: Test known values
    conversion_test1 = distance.miles_to_kilometers(1)
    np.testing.assert_allclose(conversion_test1, 1.609344, rtol = 1e-5)
        # round(1.1234,1) == 1.1

    # Test 2: Check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        distance.miles_to_kilometers(1,2)

    # Test 3: Check that 0 miles is 0 km
    assert distance.miles_to_kilometers(0) == 0

def test_kilometers_to_miles():
    # Test 1: Test known values
    conversion_test1 = distance.kilometers_to_miles(1)
    np.testing.assert_allclose(conversion_test1, 0.621371, rtol = 1e-5)

    # Test 2: Check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        distance.kilometers_to_miles(1,2)

    # Test 3: Check that 0 miles is  0 km
    assert distance.kilometers_to_miles(0) == 0
