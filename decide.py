import config
import computations
import numpy as np


def cmv_calculator(parameters, num_points, x, y):
    # Create an LIC judgement object.
    lic = computations.LaunchInterceptorConditions(parameters, num_points, x, y)

    # Iterate through all condition judgement functions in LICs.
    for function, i in zip(lic.function_list, range(15)):
        config.cmv[i] = function(lic)


def pum_calculator(cmv, lcm):
    # Calculate pum and assign it to config.
    for i in range(len(cmv)):
        for j in range(i):
            if i == j:  # diagonal element in pum
                config.pum[i][j] = cmv[i]
            elif lcm[i][j] == config.CONNECTORS[0]:  # If lcm[i][j] is "NOTUSED".
                config.pum[i][j] = config.pum[j][i] = True
            elif lcm[i][j] == config.CONNECTORS[1]:  # If lcm[i][j] is "ORR".
                config.pum[i][j] = config.pum[j][i] = cmv[i] or cmv[j]
            elif lcm[i][j] == config.CONNECTORS[2]:  # If lcm[i][j] is "ANDD".
                config.pum[i][j] = config.pum[j][i] = cmv[i] and cmv[j]
    return


def fuv_calculator(puv, pum):
    # TODO: calculate fuv and assign it to config.fuv
    for i in range(len(config.fuv)):
        if not(puv[i]) or (all(pum[i][0:i]) and all(pum[i][i+1:])):
            config.fuv[i] = True
    return



def decide(parameters=config.parameters, num_points=config.num_points,
           x=config.X, y=config.Y, lcm=config.lcm, puv=config.puv):
    # TODO: decide whether to launch the nuclear bomb or not
    cmv_calculator(parameters, num_points, x, y)
    pum_calculator(config.cmv, lcm)
    fuv_calculator(puv, config.pum)
    config.launch = all(config.fuv)
    return "YES" if config.launch else "NO"

def ghello():
    print("hej")
    config.fuv[0] = True
    return False