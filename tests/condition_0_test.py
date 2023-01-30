import unittest
import computations


class TestCondition0(unittest.TestCase):

    x = [1, 1, 5, 0, 1, 1, 4, 3, 500]
    y = [1, 1, 5, 0, 0, 1, 3, 5, 456]

    def test_distance_is_zero(self):
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 1.0},
                                                       num_points=2,
                                                       x=self.x, y=self.y)
        self.assertFalse(lic.condition_0())

    def test_not_immediately_true(self):
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 1.0},
                                                       num_points=3,
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_0())

    def test_false_distance_is_one(self):
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 1.0},
                                                       num_points=2,
                                                       x=self.x[3:5], y=self.y[3:5])
        self.assertFalse(lic.condition_0())

    def test_true_distance_is_one(self):
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 0.9},
                                                       num_points=2,
                                                       x=self.x[3:5], y=self.y[3:5])
        self.assertTrue(lic.condition_0())

    def test_true_large_distance(self):
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 30},
                                                       num_points=2,
                                                       x=self.x[7:], y=self.y[7:])
        self.assertTrue(lic.condition_0())

if __name__ == '__main__':
    unittest.main()