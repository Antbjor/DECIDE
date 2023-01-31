import unittest
import computations
import math


class TestCondition8(unittest.TestCase):

    def test_numpoints_less_than_five(self):
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(2),
                                                                   "A_PTS": 1,
                                                                   "B_PTS": 1},
                                                       num_points=2,
                                                       x=[1, 2], y=[2, 1])
        self.assertFalse(lic.condition_8())

    def test_distance_is_zero(self):
        x = [1, 3, 1, 3, 1]
        y = [1, 3, 1, 3, 1]
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(2),
                                                                   "A_PTS": 1,
                                                                   "B_PTS": 1},
                                                       num_points=5,
                                                       x=x, y=y)
        self.assertFalse(lic.condition_8())

    def test_true(self):
        x = [11, 0, 0,  3, 0, 11]
        y = [ 3, 0, 0, 11, 0,  3]
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(11),
                                                                   "A_PTS": 2,
                                                                   "B_PTS": 1},
                                                       num_points=6,
                                                       x=x, y=y)
        self.assertTrue(lic.condition_8())

    def test_zero_radius(self):
        x = [1,   3,  -51, 45,  66]
        y = [53, 32, 1234, 15, 331]
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": 0.0,
                                                                   "A_PTS": 1,
                                                                   "B_PTS": 1},
                                                       num_points=len(x),
                                                       x=x, y=y)
        self.assertTrue(lic.condition_1())

if __name__ == '__main__':
    unittest.main()
