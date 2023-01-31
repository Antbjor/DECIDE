import unittest
from unittest import TestCase
import computations


class TestCondition6(unittest.TestCase):

    x = [0, 1, 2, 3, 0, 6, 8, 8, 9, 7, 10]
    y = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 0]
    #For tests with coinciding first and last coordinates
    x_c = [0, 2, 2, 2, 0]
    y_c = [0, 2, 2, 2, 0]


    def test_points_outside_min_distance(self):
        """
        Asserts that the function returns true when a datapoint exists outside
        the minimum distance from the line drawn between two points N_PTS apart (in index).
        Tested here with a minimum distance of 1 and a line from (0,0) to (0,5) with datapoints at (1,1),
        (2,2) and (3,3).
        """
        lic = computations.LaunchInterceptorConditions(parameters={"DIST": 1,
                                                                   "N_PTS": 5},
                                                       num_points=5, x=self.x, y=self.y
                                                       )
        self.assertTrue(lic.condition_6())

    def test_points_inside_min_distance(self):
        """
        Asserts that the function returns false when no datapoint exists outside the minimum distance from
        the line drawn between two points N_PTS apart (in index).
        Tested here with a minimum distance of 4 and a line from (0,0) to (0,5) with datapoints at (1,1),
        (2,2) and (3,3).
        """
        lic = computations.LaunchInterceptorConditions(parameters={"DIST": 4,
                                                                   "N_PTS": 5},
                                                       num_points=5, x=self.x, y=self.y
                                                       )
        self.assertFalse(lic.condition_6())


    def test_first_last_coincide_outside_min_dist(self):
        """
        Asserts that the function returns true when a datapoint exists outside
        the minimum distance from the two coinciding points N_PTS apart (in index).
        Tested here with a minimum distance of 4 and a line from (0,0) to (0,5) with datapoints at (1,1),
        (2,2) and (3,3).
        """
        lic = computations.LaunchInterceptorConditions(parameters={"DIST": 2.5,
                                                                   "N_PTS": 5},
                                                       num_points=5, x=self.x_c, y=self.y_c
                                                       )
        self.assertTrue(lic.condition_6())

    def test_first_last_coincide_inside_dist(self):
        """
        Asserts that the function returns false when no datapoint exists outside
        the minimum distance from the two coinciding points N_PTS apart (in index).
        Tested here with a minimum distance of 4 and a line from (0,0) to (0,5) with datapoints at (1,1),
        (2,2) and (3,3).
        """
        lic = computations.LaunchInterceptorConditions(parameters={"DIST": 3,
                                                                   "N_PTS": 5},
                                                       num_points=5, x=self.x_c, y=self.y_c
                                                       )
        self.assertFalse(lic.condition_6())


    def test_too_few_points(self):
        """
        Asserts that the function returns false when not enough datapoints are provided,
        the requirement states num_points > 3
        """
        lic = computations.LaunchInterceptorConditions(parameters={"DIST": 1,
                                                                   "N_PTS": 3},
                                                       num_points=3, x=self.x, y=self.y
                                                       )
        self.assertFalse(lic.condition_6())
