import unittest
import computations


class TestCondition4(unittest.TestCase):
    x = [0, 0, -1, -3,   6]
    y = [0, 0,  0, -2, -10]

    def test_true_2pts_1quad_origin(self):
        lic = computations.LaunchInterceptorConditions(parameters={"Q_PTS": 2, "QUADS": 1},
                                                       num_points=2,
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_4())

    def test_false_2pts_1quad_origin(self):
        lic = computations.LaunchInterceptorConditions(parameters={"Q_PTS": 2, "QUADS": 2},
                                                       num_points=2,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_4())

    def test_true_3pts_2quad(self):
        lic = computations.LaunchInterceptorConditions(parameters={"Q_PTS": 2, "QUADS": 2},
                                                       num_points=3,
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_4())

    def test_true_3pts_3qpts_2quad(self):
        lic = computations.LaunchInterceptorConditions(parameters={"Q_PTS": 3, "QUADS": 3},
                                                       num_points=3,
                                                       x=self.x[2:], y=self.y[2:])
        self.assertTrue(lic.condition_4())

if __name__ == '__main__':
    unittest.main()
