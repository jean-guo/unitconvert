"""
A python module for converting temperatures between celsius and fahrenheit

"""
import numpy as np

def fahrenheit_to_celsius(fahrenheit_temp):
    """Calculate celsius temperature from fahrenheit

    PARAMETERS
    ----------
    fahrenheit_temp : float
        A temperature in degrees

    RETURNS
    -------
    temperature : float
    """

    # apply formula
    return (fahrenheit_temp - 32)*(5/9)

def celsius_to_fahrenheit(celsius_temp):
    """Calculate fahrenheit temperature from celsius

    PARAMETERS
    ----------
    celsius_temp : float
        A temperature in degrees

    RETURNS
    -------
    temperature : float
    """

    # apply formula
    return (celsius_temp * (9/5)) + 32
