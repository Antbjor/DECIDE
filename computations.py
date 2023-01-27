import config
import math
import numpy as np


class LaunchInterceptorConditions:
    """A class that calculates the Launch Interceptor Conditions (LICs)."""

    def __init__(self, parameters=config.parameters, num_points=config.num_points,
                 x=config.X, y=config.Y):
        self.x = x
        self.y = y
        self.num_points = num_points  # [2, 100]
        self.parameters = parameters

    def condition_0(self):
        return True

    def condition_1(self):
        return True

    def condition_2(self):
        return True

    def condition_3(self):
        return True

    def condition_4(self):
        return True

    def condition_5(self):
        return True

    def condition_6(self):
        return True

    def condition_7(self):
        return True

    def condition_8(self):
        return True

    def condition_9(self):
        return True

    def condition_10(self):
        return True

    def condition_11(self):
        return True

    def condition_12(self):
        return True

    def condition_13(self):
        return True

    def condition_14(self):
        return True

    function_list = [condition_0,  condition_1,  condition_2,  condition_3,  condition_4,
                     condition_5,  condition_6,  condition_7,  condition_8,  condition_9,
                     condition_10, condition_11, condition_12, condition_13, condition_14]
