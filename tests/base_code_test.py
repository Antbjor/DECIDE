import yaml
import config
import unittest

try:
    with open('settings.yml', encoding='utf-8') as fin:
        test_data = yaml.load(fin, Loader=yaml.FullLoader)
except FileNotFoundError:
    with open('../settings.yml', encoding='utf-8') as fin:
        test_data = yaml.load(fin, Loader=yaml.FullLoader)


class TestInputData(unittest.TestCase):
    num_points = 100  # Remember to change this parameter

    def test_num_points(self):
        self.assertEqual(config.num_points, self.num_points)
        self.assertTrue(2 <= config.num_points <= 100, "ERROR: invalid NUMPOINTS.")

    def test_point_x(self):
        point_x = test_data["POINTS_X"]
        self.assertEqual(config.X, point_x)

    def test_point_y(self):
        point_y = test_data["POINTS_Y"]
        self.assertEqual(config.Y, point_y)

    def test_lcm(self):
        for i in range(15):
            self.assertEqual(config.lcm[i][i], "ANDD", "ERROR: lcm[i, i] must be ANDD.")
            for j in range(i):
                self.assertEqual(config.lcm[i][j], config.lcm[j][i], "ERROR: lcm is not symmetric.")
        lcm = test_data["LCM"]
        self.assertEqual(config.lcm, lcm)

    def test_puv(self):
        # Remember to check puv manually before testing
        puv = ["true", "true", "true", "true", "true",
               "true", "true", "true", "true", "true",
               "true", "true", "true", "true", "true"]
        self.assertEqual(config.puv, puv)
        self.assertEqual(config.puv, test_data["PUV"])

    def test_parameters(self):
        param = config.parameters
        self.assertTrue(0 <= param["AREA1"], "ERROR: AREA1 < 0 in settings.")
        self.assertTrue(1 <= param["K_PTS"] <= param["NUMPOINTS"] - 2, "ERROR: invalid K_PTS in settings.")
        self.assertTrue(1 <= param["G_PTS"] <= param["NUMPOINTS"] - 2, "ERROR: invalid G_PTS in settings.")


if __name__ == '__main__':
    unittest.main()
