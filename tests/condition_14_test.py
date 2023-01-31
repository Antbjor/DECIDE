from unittest import TestCase

import computations


class TestCondition14(TestCase):
    x = [0, 0, 3, 1, 0, 1]
    y = [0, 0, 3, 1, 3, 0]

    x_1 = [0, 0, 3, 0, 0]
    y_1 = [0, 0, 3, 0, 3]

    def test_both_true(self):
        """
        Asserts that the function returns true when the area of a triangle created by
        the points E_PTS and F_PTS apart are greater than the AREA_1 parameter and another
        triangle with the same conditions are smaller than AREA_2" parameter in the same
        dataset.
        Tested here with a triangle with corners in (0,0), (3,3) and (0,3) and a
        parameter-value of 4 for AREA_1 and a triangle with corners in (0,0), (1,1) and (1,0)
        and a parameter-value of 1 for AREA_2
        """
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4,
                                                                   "AREA_2": 1
                                                                   },
                                                       num_points=6, x=self.x, y=self.y
                                                       )
        self.assertTrue(lic.condition_14())

    def test_only_bigger(self):
        """
        Asserts that the function returns false when the area of a triangle created by
        the points E_PTS and F_PTS apart are greater than the AREA_1 parameter but no other
        triangle with the same conditions are smaller than AREA_2" parameter in the same
        dataset.
        Tested here with a triangle with corners in (0,0), (3,3) and (0,3) and a
        parameter-value of 4 for AREA_1.
        """
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4,
                                                                   "AREA_2": 4
                                                                   },
                                                       num_points=5, x=self.x_1, y=self.y_1
                                                       )
        self.assertFalse(lic.condition_14())

    def test_only_smaller(self):
        """
        Asserts that the function returns false when the area of the triangle created by
        the points E_PTS and F_PTS apart are smaller than the AREA_2 parameter but no other
        triangle with the same conditions are bigger than AREA_1 parameter in the same
        dataset.
        Tested here with a triangle with corners in (0,0), (3,3) and (0,3) and a
        parameter-value of 4 for AREA_2
        """
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4,
                                                                   "AREA_2": 4
                                                                   },
                                                       num_points=4, x=self.x_1, y=self.y_1
                                                       )
        self.assertFalse(lic.condition_14())

    def test_too_few_points(self):
        """
        Asserts that the function returns false when not enough datapoints are provided,
        the requirement states num_points > 5
        """
        lic = computations.LaunchInterceptorConditions(parameters={"E_PTS": 1,
                                                                   "F_PTS": 1,
                                                                   "AREA_1": 4,
                                                                   "AREA_2": 4
                                                                   },
                                                       num_points=4, x=self.x, y=self.y
                                                       )
        self.assertFalse(lic.condition_14())
