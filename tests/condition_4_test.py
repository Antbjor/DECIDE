import unittest
import decide.computations as computations


class TestCondition4(unittest.TestCase):
    x = [0, 0, -1, -3,   6]
    y = [0, 0,  0, -2, -10]

    def test_true_2pts_1quad_origin(self):
        """
        Test if 2 points at the origin in the same quadrant.
        Expected outcome is true.
        """
        lic = computations.LaunchInterceptorConditions(parameters={"Q_PTS": 2, "QUADS": 1},
                                                       num_points=2,
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_4())

    def test_false_2pts_2quad_origin(self):
        """
        Test if 2 points at the origin are in two quadrants.
        Expected outcome is false.
        """
        lic = computations.LaunchInterceptorConditions(parameters={"Q_PTS": 2, "QUADS": 2},
                                                       num_points=2,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_4())

    def test_true_3pts_2quad(self):
        """
        Test if 3 points are in 2 quadrants.
        Expected outcome is true.
        """
        lic = computations.LaunchInterceptorConditions(parameters={"Q_PTS": 2, "QUADS": 2},
                                                       num_points=3,
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_4())

    def test_true_3pts_3qpts_2quad(self):
        """
        Test if 3 points are in 3 quadrants.
        Expected outcome is true.
        """
        lic = computations.LaunchInterceptorConditions(parameters={"Q_PTS": 3, "QUADS": 3},
                                                       num_points=3,
                                                       x=self.x[2:], y=self.y[2:])
        self.assertTrue(lic.condition_4())


if __name__ == '__main__':
    unittest.main()
