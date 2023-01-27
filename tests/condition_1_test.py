import config
import unittest
import computations
import math


class TestCondition1(unittest.TestCase):

    x = [1, 1, 1, 8, 5, 2, 2, 6, 2, 7, 11, 3, 11]
    y = [1, 1, 1, 2, 0, 3, 1, 3, 9, 1, 3, 11, 3]


    def test_naive_false(self):
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(2)},
                                                       num_points=3,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_1())
    
    def test_false(self):
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(130)},
                                                       num_points=3,
                                                       x=self.x[10:], y=self.y[10:])
        self.assertFalse(lic.condition_1())
    
    def test_naive_true(self):
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(2)},
                                                       num_points=3,
                                                       x=self.x[3:6], y=self.y[3:6])
        self.assertTrue(lic.condition_1())
    
    def test_true(self):
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(11)},
                                                       num_points=3,
                                                       x=self.x[10:], y=self.y[10:])
        self.assertTrue(lic.condition_1())

    def test_zero_radius(self):
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": 0.0},
                                                       num_points=len(self.x),
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_1())

if __name__ == '__main__':
    unittest.main()
