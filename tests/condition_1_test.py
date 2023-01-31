import config
import unittest
import computations
import math


class TestCondition1(unittest.TestCase):

    x = [1, 1, 1, 8, 5, 2, 2, 6, 2, 7, 11, 3, 11]
    y = [1, 1, 1, 2, 0, 3, 1, 3, 9, 1, 3, 11, 3]

    def test_naive_false(self):
        """
        Test_naive_false does check if the three points (1,1), (1,1), (1,1)
        cant be contained on a circle with a radius of math.sqrt(2)
        """ 
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(2)},
                                                       num_points=3,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_1())
    
    def test_false(self):
        """
        test_false does check if the three points (11,3), (3,11), (11,3)
        cant be contained on a circle with a radius of math.sqrt(130)
        """ 
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(130)},
                                                       num_points=3,
                                                       x=self.x[10:], y=self.y[10:])
        self.assertFalse(lic.condition_1())
    
    def test_naive_true(self):
        """
        test_naive_true does check if the three points (8,2), (5,0), (2,3)
        cant be contained on a circle with a radius of math.sqrt(2)
        """
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(2)},
                                                       num_points=3,
                                                       x=self.x[3:6], y=self.y[3:6])
        self.assertTrue(lic.condition_1())
    
    def test_true(self):
        """
        test_true does check if the three points (11,3), (3,11), (11,3)
        cant be contained on a circle with a radius of math.sqrt(11)
        """
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": math.sqrt(11)},
                                                       num_points=3,
                                                       x=self.x[10:], y=self.y[10:])
        self.assertTrue(lic.condition_1())
    
    def test_zero_radius(self):
        """
        test_zero_radius does check if any of three consecutive (x,y)
        cant be contained on a circle with a radius of 0
        """
        lic = computations.LaunchInterceptorConditions(parameters={"RADIUS1": 0.0},
                                                       num_points=len(self.x),
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_1())
    
if __name__ == '__main__':  
    unittest.main()
