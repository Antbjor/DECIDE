import unittest
import computations


class TestCondition3(unittest.TestCase):

    x = [1, 2, 4, 4, 5, 6, 8, 8, 9, 7, 10]
    y = [1, 2, 0, 4, 0, 6, 7, 8, 9, 10, 0]

    def test_lower_bound(self):
        """
        test_lower_bound tests if two points will form a triangle or not
        expected_outcome: False
        """
        lic = computations.LaunchInterceptorConditions(parameters={"AREA1": 0.0},
                                                       num_points=2,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_3())

    def test_upper_bound(self):
        """
        test_upper_bound tests if 100 data points will exceed the limit of function
        condition_3()
        expected_outcome: False
        """
        ones, zeros = [1.0 for _ in range(100)], [0.0 for _ in range(100)]
        lic = computations.LaunchInterceptorConditions(parameters={"AREA1": 0.0},
                                                       num_points=100,
                                                       x=ones, y=zeros)
        self.assertEqual(lic.condition_3(), False)

    def test_calculation_1(self):  # Test for the "negative" area
        """
        test_calculation_1 tests if the triangle area has taken absolute value
        expected_outcome: True
        """
        lic = computations.LaunchInterceptorConditions(parameters={"AREA1": 1.996},
                                                       num_points=3,
                                                       x=self.x[0:3], y=self.y[0:3])
        self.assertTrue(lic.condition_3())

    def test_calculation_2(self):
        """
        test_calculation_2 tests if the triangle area is wrongly calculated given
        only three points
        expected_outcome: False
        """
        lic = computations.LaunchInterceptorConditions(parameters={"AREA1": 5.0},
                                                       num_points=3,
                                                       x=self.x[3:6], y=self.y[3:6])
        self.assertFalse(lic.condition_3())

    def test_calculation_3(self):  # Test for more points.
        """
        test_calculation_3 tests if the triangle area is correctly calculated given
        more than three points
        expected_outcome: True
        """
        lic = computations.LaunchInterceptorConditions(parameters={"AREA1": 8.0},
                                                       num_points=5,
                                                       x=self.x[6:11], y=self.y[6:11])
        self.assertTrue(lic.condition_3())


if __name__ == '__main__':
    unittest.main()
