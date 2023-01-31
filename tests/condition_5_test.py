import unittest
import decide.computations as computations


class TestCondition5(unittest.TestCase):
    x = [1, 1, 1, 8, 5, 2, 2, 6, 2, 7, 11, 3, 11]
    y = [1, 1, 1, 2, 0, 3, 1, 3, 9, 1, 3, 11, 3]

    def test_ascending(self):
        """
        test_ascending does check if two consecutive points out of points sorted in ascending order
        are sorted in descending order
        """
        lic = computations.LaunchInterceptorConditions(parameters=None,
                                                       num_points=len(self.x),
                                                       x=sorted(self.x), y=self.y)
        self.assertFalse(lic.condition_5())

    def test_descending(self):
        """
        test_descending does check if two consecutive points out of points sorted in descending order
        are sorted in descending order
        """
        lic = computations.LaunchInterceptorConditions(parameters=None,
                                                       num_points=len(self.x),
                                                       x=sorted(self.x, reverse=True), y=self.y)
        self.assertTrue(lic.condition_5())

    def test_equal(self):
        """
        test_equal does check if two consecutive points out of three equivalent points
        are sorted in descending order
        """
        lic = computations.LaunchInterceptorConditions(parameters=None,
                                                       num_points=3,
                                                       x=self.x[0:3], y=self.y)
        self.assertFalse(lic.condition_5())

    def test_un_sorted(self):
        """
        test_un_sorted does check if two consecutive points out of (x,y) 
        are sorted in descending order
        """
        lic = computations.LaunchInterceptorConditions(parameters=None,
                                                       num_points=len(self.x),
                                                       x=self.x, y=self.y)
        self.assertTrue(lic.condition_5())


if __name__ == '__main__':
    unittest.main()
