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
        """
        Return true if three consecutive data points cannot be contained on a circle with radius RADIUS1
        """
        consecutive_data_points = 0
        for i in range(self.num_points):
            if math.dist([0,0], [self.x[i], self.y[i]]) != self.parameters["RADIUS1"]:
                consecutive_data_points += 1
                if consecutive_data_points == 3:
                    return True
            else:
                consecutive_data_points = 0
        return False

    def condition_2(self):
        return True

    def condition_3(self):
        # special cases
        if self.num_points == 2:
            return False
        # regular cases
        for i in range(self.num_points - 2):
            area = abs(self.x[i] * (self.y[i + 1] - self.y[i + 2])
                       + self.x[i + 1] * (self.y[i + 2] - self.y[i])
                       + self.x[i + 2] * (self.y[i] - self.y[i + 1])) / 2
            if area > self.parameters["AREA1"]:
                return True
        return False

    def condition_4(self):
        return True

    def condition_5(self):
        for i in range(self.num_points-1):
            if self.x[i] > self.x[i+1]:
                return True
        return False

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
