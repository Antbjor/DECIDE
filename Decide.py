import numpy as np
import math

# Constant
pi = float(3.1415926535)

# Type declarations
CONNECTORS = ["NOTUSED", "ORR", "ANDD"]  # in requirements NOTUSED=777
COMPTYPE = ["LT", "EQ", "GT"]  # in requirements LT=1111

""" pointers are not used in python
    global COORDINATE  # pointer to an array of 100 doubles
    global CMATRIX  # pointer to a 2-D array of [15,15] CONNECTORS
    global BMATRIX  # pointer to 2-D array of [15,15]  booleans
    global VECTOR  # pointer to an array of 15 booleans
"""

# Global variable declaration
global X, X2, Y, Y2  # COORDINATES X,Y
global NUMPOINTS, NUMPOINTS2  # Number of datapoints
global LCM, LCM2  # Logical Connector Matrix
global CMV, CMV2  # Conditions Met Vector
global FUV, FUV2  # Final Unlocking Vector
global LAUNCH, LAUNCH2  # Decision: Launch or No Launch


# Inputs (input object) to the DECIDE() function
class ParametersT:
    # Doubles in requirements same precision as float() in python
    LENGTH1 = 0.0  # Length in LIC 0, 7, 12
    RADIUS1 = 0.0  # Radius in LIC 1, 8, 13
    EPSILON = 0.0  # Deviation from PI in LIC 2, 9
    AREA1 = 0.0  # Area in LIC 3, 10, 14
    DIST = 0.0  # Distance in LIC 6
    LENGTH2 = 0.0  # Maximum length in LIC 12
    RADIUS2 = 0.0  # Maximum length in LIC 13
    AREA2 = 0.0  # Maximum length in LIC 14

    # Ints in requirements
    Q_PTS = 0  # Number of consecutive points in LIC 4
    QUADS = 0  # Number of quadrants in LIC 4
    N_PTS = 0  # Number of consecutive points in LIC 6
    K_PTS = 0  # Number of int points in LIC 7, 12
    A_PTS = 0  # Number of int points in LIC 8, 13
    B_PTS = 0  # Number of int points in LIC 8, 13
    C_PTS = 0  # Number of int points in LIC 9
    D_PTS = 0  # Number of int points in LIC 9
    E_PTS = 0  # Number of int points in LIC 10, 14
    F_PTS = 0  # Number of int points in LIC 10, 14
    G_PTS = 0  # Number of int points in LIC 11


global parameters
# parameters = ParametersT


# Compares floating point numbers
def DOUBLECOMPARE(a, b):
    if abs(float(a) - float(b)) < 0.000001:
        return "EQ"
    if a < b:
        return "LT"
    return "GT"
