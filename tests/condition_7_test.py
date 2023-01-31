import unittest
import computations


class TestCondition7(unittest.TestCase):  # Test class for condition 7

    x = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]
    y = [0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]
    x_p = [0, -1, 0, 1, 0, -1, 0, 11, 0, -1, 0, 1, 0, -1, 0]
    y_p = [0, -1, 0, 1, 0, -1, 0, 11, 0, -1, 0, 1, 0, -1, 0]

    def test_lower_bound(self):
        """
        test_lower_bound tests if two points can be seperated by K_PTS consecutive points

        expected_outcome: False
        """
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 0.0, "K_PTS": 1},
                                                       num_points=2,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_7())

    def test_upper_bound(self):
        """
        test_upper_bound tests if 100 points will exceed the limit of function
        condition_7()

        expected_outcome_1: False
        expected_outcome_2: True
        """
        ones, zeros = [1.0 for _ in range(100)], [0.0 for _ in range(100)]
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 0.0, "K_PTS": 98},
                                                       num_points=100,
                                                       x=ones, y=zeros)
        self.assertEqual(lic.condition_7(), False)
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 1.0, "K_PTS": 98},
                                                       num_points=100,
                                                       x=ones, y=zeros)
        ones[99], zeros[99] = 0.0, 1.0
        self.assertEqual(lic.condition_7(), True)

    def test_oscillation(self):
        """
        test_oscillation tests if the oscillating points will meet the requirement that the
        distance of two K_PTS consecutive points is longer than LENGTH1 given small K_PTS

        expected_outcome: False
        """
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 0.0, "K_PTS": 3},
                                                       num_points=11,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_7())

    def test_impulse(self):
        """
        test_impulse tests if the pulse points will meet the requirement that the distance
        of two K_PTS consecutive points is longer than LENGTH1 given different K_PTS

        expected_outcome_1: False
        expected_outcome_2: True
        expected_outcome_3: True
        """
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 6.6, "K_PTS": 7},
                                                       num_points=15,
                                                       x=self.x_p, y=self.y_p)
        self.assertFalse(lic.condition_7())
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 6.6, "K_PTS": 6},
                                                       num_points=15,
                                                       x=self.x_p, y=self.y_p)
        self.assertTrue(lic.condition_7())
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 6.6, "K_PTS": 1},
                                                       num_points=15,
                                                       x=self.x_p, y=self.y_p)
        self.assertTrue(lic.condition_7())

    def test_simple_calculation(self):
        """
        test_simple_calculation tests if the different point sets will meet the requirement that
        the distance of two K_PTS consecutive points is longer than LENGTH1 given different K_PTS

        expected_outcome_1: True
        expected_outcome_2: False
        expected_outcome_3: False
        expected_outcome_4: True
        """
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 1.996, "K_PTS": 1},
                                                       num_points=5,
                                                       x=self.x[0:6], y=self.y[0:6])
        self.assertTrue(lic.condition_7())
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 2.0, "K_PTS": 1},
                                                       num_points=5,
                                                       x=self.x[0:6], y=self.y[0:6])
        self.assertFalse(lic.condition_7())
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 1.5, "K_PTS": 2},
                                                       num_points=5,
                                                       x=self.x[0:5], y=self.y[0:5])
        self.assertFalse(lic.condition_7())
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 1.414, "K_PTS": 2},
                                                       num_points=5,
                                                       x=self.x[0:5], y=self.y[0:5])
        self.assertTrue(lic.condition_7())


if __name__ == '__main__':
    unittest.main()
