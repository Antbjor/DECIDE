import unittest
import decide.computations as computations


class TestCondition2(unittest.TestCase):
    x = [1, 0, 0, 4, 5, 6, 8, 8, 9, 7, 10]
    y = [0, 0, 1, 4, 0, 6, 7, 8, 9, 10, 0]

    def test_incorrect_epsilon(self):
        """
        Asserts that an Epsilon too large raises a type error, tested here with
        epsilon = 3.2.
        """
        lic = computations.LaunchInterceptorConditions(parameters={"EPSILON": 3.2},
                                                       num_points=11, x=self.x, y=self.y
                                                       )
        with self.assertRaises(TypeError, msg="Epsilon must fulfill 0 < Epsilon < pi"):
            lic.condition_2()

    def test_too_few_points(self):
        """
        Asserts that the function returns false if there are not enough datapoints,
        tested here with 2 datapoints and the minimum should be 3.
        """
        lic = computations.LaunchInterceptorConditions(num_points=2, x=self.x, y=self.y)
        self.assertFalse(lic.condition_2())

    def test_angle_small_enough(self):
        """
        Asserts that the function returns true for an accepted angle, tested here with
        an 90-degree angle between (1,0), (0,0) and (0,1). The condition is
        angle < pi - epsilon, here 1.57 < 3.14 - 1.
        """
        lic = computations.LaunchInterceptorConditions(parameters={"EPSILON": 1.0},
                                                       num_points=3, x=self.x, y=self.y)

        self.assertTrue(lic.condition_2())

    def test_angle_too_big(self):
        """
        Asserts that the function returns false for an incorrect angle, tested here with
        an 90-degree angle between (1,0), (0,0) and (0,1). The condition is
        angle < pi - epsilon, here 1.57 < 3.14 - 2.
        """
        lic = computations.LaunchInterceptorConditions(parameters={"EPSILON": 2.0},
                                                       num_points=3, x=self.x, y=self.y)

        self.assertFalse(lic.condition_2())
