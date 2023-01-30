from unittest import TestCase

import computations


class TestCondition14(TestCase):
    x = [0, 0, 3, 1, 0, 1]
    y = [0, 0, 3, 1, 3, 0]

    x_1 = [0, 0, 3, 0, 0]
    y_1 = [0, 0, 3, 0, 3]

    def test_both_true(self):
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4,
                                                                   "AREA_2": 1
                                                                   },
                                                       num_points=6, x=self.x, y=self.y
                                                       )
        self.assertTrue(lic.condition_14())

    def test_only_bigger(self):
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4,
                                                                   "AREA_2": 4
                                                                   },
                                                       num_points=5, x=self.x_1, y=self.y_1
                                                       )
        self.assertFalse(lic.condition_14())

    def test_only_smaller(self):
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4,
                                                                   "AREA_2": 4
                                                                   },
                                                       num_points=4, x=self.x_1, y=self.y_1
                                                       )
        self.assertFalse(lic.condition_14())

    def test_too_few_points(self):
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4,
                                                                   "AREA_2": 4
                                                                   },
                                                       num_points=4, x=self.x, y=self.y
                                                       )
        self.assertFalse(lic.condition_14())
