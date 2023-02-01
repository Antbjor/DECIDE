import decide.config as config
import unittest


class TestInputData(unittest.TestCase):
    """
    This class is used to test the Input Data in the data.yml

    :param: unittest.TestCase
    """

    def test_num_points(self):
        """
        This function tests and ensures that the number_of_points in data file is
        within the range of [2, 100].

        :return: nothing
        """
        self.assertTrue(2 <= config.num_points <= 100, "ERROR: invalid NUMPOINTS.")

    def test_data_points(self):
        """
        This function tests and ensures that the number of data points in data file
        is smaller than the number_of_points in data file.

        :return: nothing
        """
        self.assertTrue(config.num_points <= len(config.X), "ERROR: POINTS_X < NUMPOINTS.")
        self.assertTrue(config.num_points <= len(config.Y), "ERROR: POINTS_Y < NUMPOINTS.")

    def test_lcm(self):
        """
        This function tests and ensures that the input lcm in data file is symmetry.

        :return: nothing
        """
        for i in range(15):
            self.assertEqual(config.lcm[i][i], "ANDD", "ERROR: lcm[i, i] must be ANDD.")
            for j in range(i):
                self.assertEqual(config.lcm[i][j], config.lcm[j][i], "ERROR: lcm is not symmetric.")

    def test_parameters(self):
        """
        This function tests and ensures that some crucial parameters in data file
        are valid.

        :return: nothing
        """
        param = config.parameters
        self.assertTrue(0 <= param["AREA1"], "ERROR: AREA1 < 0 in settings.")
        self.assertTrue(1 <= param["K_PTS"] <= config.num_points - 2, "ERROR: invalid K_PTS in settings.")
        self.assertTrue(1 <= param["G_PTS"] <= config.num_points - 2, "ERROR: invalid G_PTS in settings.")


if __name__ == '__main__':
    unittest.main()
