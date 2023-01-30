import unittest
from unittest import TestCase

import computations


class TestCondition10(unittest.TestCase):
    x = [0, 0, 3, 0, 0]
    y = [0, 0, 3, 0, 3]

    # Test with coinciding coordinates
    x_c = [0, 0, 3, 0, 3]
    y_c = [0, 0, 3, 0, 3]

    def test_area_bigger(self):
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4
                                                                   },
                                                       num_points=5, x=self.x, y=self.y
                                                       )
        self.assertTrue(lic.condition_10())

    def test_area_smaller(self):
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 5
                                                                   },
                                                       num_points=5, x=self.x, y=self.y
                                                       )
        self.assertFalse(lic.condition_10())

    def test_not_a_triangle(self):
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 5
                                                                   },
                                                       num_points=5, x=self.x_c, y=self.y_c
                                                       )
        self.assertFalse(lic.condition_10())

    def test_too_few_points(self):
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 5
                                                                   },
                                                       num_points=3, x=self.x, y=self.y
                                                       )
        self.assertFalse(lic.condition_10())