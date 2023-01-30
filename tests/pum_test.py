import config
import decide
import unittest

decide.cmv_calculator(config.parameters, config.num_points, config.X, config.Y)
decide.pum_calculator(config.cmv, config.lcm)


class TestPUMFunction(unittest.TestCase):

    def test_pum_size(self):
        pum_row = len(config.pum)
        self.assertEqual(len(config.cmv), pum_row, "ERROR: wrong pum row.")
        for i in range(pum_row):
            self.assertEqual(len(config.cmv), len(config.pum[i]), "ERROR: wrong pum column.")

    def test_symmetry(self):
        for i in range(len(config.cmv)):
            self.assertEqual(config.pum[i][i], config.cmv[i], "ERROR: pum[i, i] must be cmv[i].")
            for j in range(i):
                self.assertEqual(config.pum[i][j], config.pum[j][i], "ERROR: pum is not symmetric.")

    def test_value(self):
        # Remember to check pum manually before testing
        pum = config.pum  # Need to replace afterwards.
        self.assertEqual(config.pum, pum)


if __name__ == '__main__':
    unittest.main()
