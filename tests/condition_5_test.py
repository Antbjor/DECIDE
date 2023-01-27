import config
import unittest
import computations


class TestCondition5(unittest.TestCase):

    x = [1, 1, 1, 8, 5, 2, 2, 6, 2, 7, 11, 3, 11]
    y = [1, 1, 1, 2, 0, 3, 1, 3, 9, 1, 3, 11, 3]

    def test_ascending(self):
        lic = computations.LaunchInterceptorConditions(parameters=None,
                                                       num_points=len(self.x),
                                                       x=sorted(self.x), y=self.y)
        self.assertFalse(lic.condition_5())

    def test_descending(self):
        lic = computations.LaunchInterceptorConditions(parameters=None,
                                                       num_points=len(self.x),
                                                       x=sorted(self.x, reverse=True), y=self.y)
        self.assertTrue(lic.condition_5())

    def test_equal(self):
        lic = computations.LaunchInterceptorConditions(parameters=None,
                                                       num_points=3,
                                                       x=self.x[0:3], y=self.y)
        self.assertFalse(lic.condition_5())

    def test_un_sorted(self):
        lic = computations.LaunchInterceptorConditions(parameters=None,
                                                       num_points=len(self.x),
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_5())

if __name__ == '__main__':
    unittest.main()
