import unittest

import computations


class TestCondition2(unittest.TestCase):
    x = [1, 0, 0, 4, 5, 6, 8, 8, 9, 7, 10]
    y = [0, 0, 1, 4, 0, 6, 7, 8, 9, 10, 0]

    def test_incorrect_epsilon(self):
        lic = computations.LaunchInterceptorConditions(parameters={"EPSILON": 3.2},
                                                       num_points=2, x=self.x, y=self.y
                                                       )
        with self.assertRaises(TypeError, msg="Epsilon must fulfill 0 < Epsilon < pi"):
            lic.condition_2()

    def test_too_few_points(self):
        lic = computations.LaunchInterceptorConditions(num_points=2, x=self.x, y=self.y)
        self.assertFalse(lic.condition_2())

    def test_angle_small_enough(self):
        lic = computations.LaunchInterceptorConditions(parameters={"EPSILON": 1.0},
                                                       num_points=3, x=self.x, y=self.y)

        self.assertTrue(lic.condition_2())

    def test_angle_too_big(self):
        lic = computations.LaunchInterceptorConditions(parameters={"EPSILON": 2.0},
                                                       num_points=3, x=self.x, y=self.y)

        self.assertFalse(lic.condition_2())
