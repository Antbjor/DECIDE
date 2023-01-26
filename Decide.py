from array import array
import numpy as np

#Constant
pi = float(3.1415926535)

#Type declarations
CONNECTORS = ["NOTUSED", "ORR", "ANDD"] #in requirements NOTUSED=777
COMPTYPE = ["LT", "EQ", "GT"]           #in requirements LT=1111

global COORDINATE   #pointer to an array of 100 doubles
global CMATRIX      #pointer to a 2-D array of [15,15] CONNECTORS
global BMATRIX      #pointer to 2-D array of [15,15]  booleans
global VECTOR       #pointer to an array of 15 booleans

#Global variable declaration
global X, X2, Y, Y2             #COORDINATES X,Y
global NUMPOINTS, NUMPOINTS2    #Number of datapoints
global LCM, LCM2                #Logical Connector Matrix
global CMV, CMV2                #Conditions Met Vector
global FUV, FUV2                #Final Unlocking Vector
global LAUNCH, LAUNCH2          #Decision: Launch or No Launch


#Inputs to the DECIDE() function
global LENGTH1, RADIUS1, EPSILON, AREA1, DIST, LENGTH2, RADIUS2, AREA2 #Doubles in requirements same precision as float() in python
global Q_PTS, QUADS, N_PTS, K_PTS, A_PTS, B_PTS, C_PTS, D_PTS, E_PTS, F_PTS, G_PTS #Ints in requirements

#Compares floating point numbers
def DOUBLECOMPARE(a, b):
    if(abs(float(a) - float(b)) < 0.000001):
        return "EQ"
    if (a<b):
        return "LT"
    return "GT"



