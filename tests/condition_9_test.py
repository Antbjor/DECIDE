import config
import unittest
import computations


class TestCondition9(unittest.TestCase):

    x = [1, 2, 3, 4, 5, 2, 8, 6, 2, 7, 11, 3, 11]
    y = [0, 2, 0, 4, 0, 3, 1, 3, 9, 1, 3, 11, 3]

    def test_angle_equal_pi(self):
        lic = computations.LaunchInterceptorConditions(parameters={"C_PTS": 1, "D_PTS": 1, "EPSILON": 0},
                                                       num_points=5,
                                                       x=self.x[0:5], y=self.y[0:5])
        self.assertFalse(lic.condition_9())
    
    
    def test_less_than_five_points(self):
        lic = computations.LaunchInterceptorConditions(parameters={"C_PTS": 1, "D_PTS": 1, "EPSILON": 0},
                                                       num_points=4,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_9())
    
    def test_angle_bigger(self):
        lic = computations.LaunchInterceptorConditions(parameters={"C_PTS": 2, "D_PTS": 2, "EPSILON": -3},
                                                       num_points=len(self.x),
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_9())
    
    def test_angle_smaller(self):
        lic = computations.LaunchInterceptorConditions(parameters={"C_PTS": 3, "D_PTS": 3, "EPSILON": 0},
                                                       num_points=len(self.x),
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_9())
    
    def test_points_coincide(self):
        lic = computations.LaunchInterceptorConditions(parameters={"C_PTS": 1, "D_PTS": 1, "EPSILON": 0},
                                                       num_points=len(self.x[8:]),
                                                       x=self.x[8:], y=self.y[8:])
        self.assertFalse(lic.condition_9())

if __name__ == '__main__':
    unittest.main()
