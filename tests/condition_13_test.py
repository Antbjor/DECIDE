import config
import unittest
import computations
import math


class TestCondition13(unittest.TestCase):

    x = [2, 1, 3, 8, 3, 2, 2, 6, 2, 7, 11, 3, 11]
    y = [1, 1, 3, 2, 3, 3, 1, 3, 9, 1, 3, 11, 3]

    
    def test_radius1_circle(self):
        """
        test_radius1_circle does check if the three points out of (2,1), (1,1), (3,3), (8,2), (3,3), 
        separated by 1 and 1 points, that cant be contained on a circle with a radius of 1 but can be contained on circle with radius 1
        """ 
        lic = computations.LaunchInterceptorConditions(parameters={"A_PTS": 1, "B_PTS": 1, 
                                                                   "RADIUS1": 1, "RADIUS2": 1},
                                                       num_points=len(self.x[0:5]),
                                                       x=self.x[0:5], y=self.y[0:5])
        self.assertFalse(lic.condition_13())
    
    def test_radius2_circle(self):
        """
        test_radius2_circle does check if the three points out of (2,1), (1,1), (3,3), (8,2), (3,3), 
        separated by 1 and 1 points, that cant be contained on a circle with a radius of 3 but can be contained on circle with radius 2
        """ 
        lic = computations.LaunchInterceptorConditions(parameters={"A_PTS": 1, "B_PTS": 1, 
                                                                   "RADIUS1": 3, "RADIUS2": 2},
                                                       num_points=len(self.x[0:5]),
                                                       x=self.x[0:5], y=self.y[0:5])
        self.assertFalse(lic.condition_13())
    
    def test_radius_1_2_circle(self):
        """
        test_radius_1_2_circle does check if the three points out of (2,1), (1,1), (3,3), (8,2), (3,3), 
        separated by 1 and 1 points, that cant be contained on a circle with a radius of 1 but can be contained on circle with radius 2
        """ 
        lic = computations.LaunchInterceptorConditions(parameters={"A_PTS": 1, "B_PTS": 1, 
                                                                   "RADIUS1": 1, "RADIUS2": 2},
                                                       num_points=len(self.x[0:5]),
                                                       x=self.x[0:5], y=self.y[0:5])
        self.assertTrue(lic.condition_13())
    
    
    def test_less_than_5_numpoints(self):
        """
        test_less_than_5_numpoints does check if the function can accept an input of less than five data points
        """
        lic = computations.LaunchInterceptorConditions(parameters={"A_PTS": 1, "B_PTS": 1, 
                                                                   "RADIUS1": math.sqrt(2), "RADIUS2": math.sqrt(2)},
                                                       num_points=4,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_13())
if __name__ == '__main__':
    unittest.main()
