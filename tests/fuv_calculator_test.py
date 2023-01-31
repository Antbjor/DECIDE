import config
import unittest
import decide

decide.cmv_calculator(config.parameters, config.num_points, config.X, config.Y)
decide.pum_calculator(config.cmv, config.lcm)
decide.fuv_calculator(config.puv, config.pum)


class TestFuvFunction(unittest.TestCase):
    
    def test_fuv_size(self):
        """
        test_fuv_size tests if the size of puv vector is the same as fuv vector.

        expected_outcome: True
        """
        self.assertEqual(len(config.puv), len(config.fuv), "ERROR: size difference.")

    def test_fuv_true_puv_false(self):
        """
        test_fuv_true_puv_false tests the situation that fuv vector is true but puv is false.

        expected_outcome: True
        """
        for i in range(len(config.fuv)):
            if not(config.puv[i]):
                self.assertTrue(config.fuv[i])


if __name__ == '__main__':  
    unittest.main()
