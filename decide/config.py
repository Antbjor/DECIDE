import os
import yaml

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    with open(os.path.join(dir_path, 'data.yml'), encoding='utf-8') as fin:
        data = yaml.load(fin, Loader=yaml.FullLoader)
except FileNotFoundError:
    try:
        with open('data.yml', encoding='utf-8') as fin:
            data = yaml.load(fin, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print("ERROR: File 'data.yml' not found! "
              "Please ensure that 'data.yml' exists in the directory "
              "'DECIDE/decide' or in your current working directory! ")
        exit(1)

# Constant
PI = float(3.1415926535)

# Enumeration type definition
CONNECTORS = ("NOTUSED", "ORR", "ANDD")  # in requirements NOTUSED=777
COMP_TYPE = ("LT", "EQ", "GT")  # in requirements LT=1111

# Global variable declaration
X, Y = data["POINTS_X"], data["POINTS_Y"]  # COORDINATES X,Y
global X2, Y2

num_points = data["NUMPOINTS"]  # Number of datapoints
global num_points_2

lcm = data["LCM"]  # Logical Connector Matrix
global lcm2

puv = data["PUV"]  # Preliminary Unlocking Vector
global puv2

pum = [[False for _ in range(15)] for _ in range(15)]  # Preliminary Unlocking Matrix
global pum2

cmv = [False for _ in range(15)]  # Conditions Met Vector
global cmv2

fuv = [False for _ in range(15)]  # Final Unlocking Vector
global fuv2

global launch  # Decision: Launch or No Launch

# Inputs to the DECIDE() function
parameters = data["PARAMETERS"]


# Compares floating point numbers
def double_compare(a, b):
    if abs(float(a) - float(b)) < 0.000001:
        return "EQ"
    if a < b:
        return "LT"
    return "GT"
