"""
A python module for converting distances between miles and kilometers

"""
import numpy as np

def miles_to_kilometers(miles):
    """Convert miles to kilometers

    PARAMETERS
    ----------
    miles : float
        A distance in miles

    RETURNS
    -------
    distance : float
    """

    # apply formula
    return miles*1.609344

def kilometers_to_miles(kilo):
    """Convert kilometers to miles

    PARAMETERS
    ----------
    kilo : float
        A distance in kilometers

    RETURNS
    -------
    distance : float
    """

    # apply formula
    return kilo*0.621371 
