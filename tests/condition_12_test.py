import unittest
import computations


class TestCondition12(unittest.TestCase):

    def test_distance_zero_kpts_zero(self):
        x = [1, 1, 5, 0, 1, 1, 4, 3, 500]
        y = [1, 1, 5, 0, 0, 1, 3, 5, 456]
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 1.0,
                                                                   "LENGTH2": 1.0,
                                                                   "K_PTS": 0},
                                                       num_points=2,
                                                       x=x, y=y)
        self.assertFalse(lic.condition_12())

    def test_true_kpts_one(self):
        x = [4, 3, 500]
        y = [3, 5, 456]
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 3.0,
                                                                   "LENGTH2": 5.0,
                                                                   "K_PTS": 1},
                                                       num_points=len(x),
                                                       x=x, y=y)
        self.assertTrue(lic.condition_12())

    def test_false_length1_kpts_one(self):
        x = [4, 3, 500]
        y = [3, 5, 456]
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 3.0,
                                                                   "LENGTH2": 1000.0,
                                                                   "K_PTS": 1},
                                                       num_points=len(x),
                                                       x=x, y=y)
        self.assertFalse(lic.condition_12())

    def test_false_length2_kpts_one(self):
        x = [4, 3, 500]
        y = [3, 5, 456]
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 1000.0,
                                                                   "LENGTH2": 5.0,
                                                                   "K_PTS": 1},
                                                       num_points=len(x),
                                                       x=x, y=y)
        self.assertFalse(lic.condition_12())

    def test_true_kpts_three(self):
        x = [4, 4, 6, 7, 3, 500]
        y = [3, 4, 6, 6, 5, 456]
        lic = computations.LaunchInterceptorConditions(parameters={"LENGTH1": 3.0,
                                                                   "LENGTH2": 5.0,
                                                                   "K_PTS": 3},
                                                       num_points=len(x),
                                                       x=x, y=y)
        self.assertTrue(lic.condition_12())
        
if __name__ == '__main__':
    unittest.main()