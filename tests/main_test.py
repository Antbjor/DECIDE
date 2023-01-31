import os
import yaml
import unittest
import decide.config as config
import decide.decision as decision

dir_path = os.path.dirname(os.path.realpath(__file__))
data = []

# Constant
NUM_TESTCASES = 3  # Number of testcases to test.
LAUNCH_ONLY = True  # Only test the final result.

for i in range(NUM_TESTCASES):
    file_name = 'test_case_' + str(i) + '.yml'
    try:
        with open(os.path.join(dir_path, file_name), encoding='utf-8') as fin:
            data.append(yaml.load(fin, Loader=yaml.FullLoader))
    except FileNotFoundError:
        print("ERROR: File '" + file_name + "' not found! "
              "Please ensure that 'data.yml' exists in the directory 'DECIDE/tests'.")
        exit(1)


class TestInputData(unittest.TestCase):
    """
    This class is used to test the main function 'decide()' in the 'decide' package

    All test cases are read from 'test_case_n.yml' in 'DECIDE/tests'
    """

    if LAUNCH_ONLY:  # Intermediate outputs will NOT be tested in this case.

        def test_launch_only(self):
            """
            This function tests and ensures that final launch decision is the same as expected.
            """
            expected_launch_result = ["False", "False", "True"]  # Change according to real situation.
            launch_decision = []

            for j in range(NUM_TESTCASES):
                decision.decide(parameters=data[j]["PARAMETERS"], num_points=data[j]["NUMPOINTS"],
                                x=data[j]["POINTS_X"], y=data[j]["POINTS_Y"],
                                lcm=data[j]["LCM"], puv=data[j]["PUV"])
                launch_decision.append(config.launch)

            self.assertEqual(launch_decision, expected_launch_result, "ERROR: Wrong results.")

    else:

        def __test_cmv_output__(self, parameters, num_points, x, y):
            """
            This function tests and ensures that the intermediate output cmv is correct.
            """
            decision.cmv_calculator(parameters, num_points, x, y)
            expected_cmv = []  # Change according to the specific case you want to test.
            self.assertEqual(config.cmv, expected_cmv, "ERROR: Wrong cmv results.")

        def __test_pum_output__(self, cmv, lcm):
            """
            This function tests and ensures that the intermediate output pum is correct.
            """
            decision.pum_calculator(cmv=cmv, lcm=lcm)
            expected_pum = [[]]  # Change according to the specific case you want to test.
            self.assertEqual(config.pum, expected_pum, "ERROR: Wrong pum results.")

        def __test_fuv_output__(self, puv, pum):
            """
            This function tests and ensures that the intermediate output fuv is correct.
            """
            decision.fuv_calculator(puv=puv, pum=pum)
            expected_fuv = []  # Change according to the specific case you want to test.
            self.assertEqual(config.fuv, expected_fuv, "ERROR: Wrong fuv results.")

        def test_launch(self):
            """
            This function tests and ensures that final launch decision is the same as expected.
            """
            test_case_id = 0  # Change the specific test case id.
            expected_launch_result = "False"  # Change according to the specific case you want to test.

            test_data = data[test_case_id]
            self.__test_cmv_output__(parameters=test_data["PARAMETERS"],
                                     num_points=test_data["NUMPOINTS"],
                                     x=test_data["POINTS_X"], y=test_data["POINTS_Y"])
            self.__test_pum_output__(cmv=config.cmv, lcm=test_data["LCM"])
            self.__test_fuv_output__(puv=test_data["PUV"], pum=config.pum)
            config.launch = all(config.fuv)

            self.assertEqual(config.launch, expected_launch_result, "ERROR: Wrong results.")


if __name__ == '__main__':
    unittest.main()
