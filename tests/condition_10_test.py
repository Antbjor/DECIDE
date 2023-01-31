import unittest
from unittest import TestCase

import decide.computations as computations


class TestCondition10(unittest.TestCase):
    x = [0, 0, 3, 0, 0]
    y = [0, 0, 3, 0, 3]

    # Test with coinciding coordinates
    x_c = [0, 0, 3, 0, 3]
    y_c = [0, 0, 3, 0, 3]

    def test_area_bigger(self):
        """
        Asserts that the function returns true when the area of the triangle created by
        the points E_PTS and F_PTS apart are greater than the AREA_1 parameter.
        Tested here with a triangle with corners in (0,0), (3,3) and (0,3) and a
        parameter-value of 4 for AREA_1
        """
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4
                                                                   },
                                                       num_points=5, x=self.x, y=self.y
                                                       )
        self.assertTrue(lic.condition_10())

    def test_area_smaller(self):
        """
        Asserts that the function returns false when the area of the triangle created by
        the points E_PTS and F_PTS apart are smaller than the AREA_1 parameter.
        Tested here with a triangle with corners in (0,0), (3,3) and (0,3) and a
        parameter-value of 5 for AREA_1
        """
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 5
                                                                   },
                                                       num_points=5, x=self.x, y=self.y
                                                       )
        self.assertFalse(lic.condition_10())

    def test_not_a_triangle(self):
        """
        Asserts that the function returns false when the datapoints does not
        form an triangle
        """
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 5
                                                                   },
                                                       num_points=5, x=self.x_c, y=self.y_c
                                                       )
        self.assertFalse(lic.condition_10())

    def test_too_few_points(self):
        """
        Asserts that the function returns false when not enough datapoints are provided,
        the requirement states num_points > 5
        """
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 5
                                                                   },
                                                       num_points=3, x=self.x, y=self.y
                                                       )
        self.assertFalse(lic.condition_10())