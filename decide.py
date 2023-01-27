import config
import computations
import numpy as np


def cmv_calculator(parameters, num_points, x, y):
    # Create an LIC judgement object.
    lic = computations.LaunchInterceptorConditions(parameters, num_points, x, y)

    # Iterate through all condition judgement functions in LICs.
    for function, i in zip(lic.function_list, range(15)):
        config.cmv[i] = function()


def pum_calculator(cmv, lcm):
    # TODO: calculate pum and assign it to config.pum
    pass


def fuv_calculator(puv, pum):
    # TODO: calculate fuv and assign it to config.fuv
    pass


def decide(parameters=config.parameters, num_points=config.num_points,
           x=config.X, y=config.Y, lcm=config.lcm, puv=config.puv):
    # TODO: decide whether to launch the nuclear bomb or not
    cmv_calculator(parameters, num_points, x, y)
    pum_calculator(config.cmv, lcm)
    fuv_calculator(puv, config.pum)
    config.launch = all(config.fuv)
    return "YES" if config.launch else "NO"
