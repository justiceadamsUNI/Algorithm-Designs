## Author:   Justice Adams
## Unit test for knapsack_problem script

## You must have installed the libraries mock
## (https://docs.python.org/dev/library/unittest.mock.html) for this
## test to be fully functional/exhaustive.

import unittest
from unittest import mock
import random
from mock import patch
import knapsack_problem


class TestKnapsackProblem(unittest.TestCase):
    weights = [1,2,5]
    values = [20,20,45]
    capacity = 7

    def setUp(self):
        print("Testing: ", self._testMethodName)


    def test_fillKnapsack(self):
        most_valuable_knapsack = knapsack_problem.fillKnapsack(self.weights,
                                                               self.values,
                                                               self.capacity)

        assertListsEqual(self, most_valuable_knapsack, [0,2])


    def test_computePowerSet(self):
        power_set = knapsack_problem.computePowerset([1,2,3])
        expected_power_set = [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]

        assertListsEqual(self, power_set, expected_power_set)


    def test_getAllValidKnapsackCombinations(self):
        empty_knapsack = []
        valid_knapsack1 = [0,2]
        valid_knapsack2 = [0,1]
        valid_knapsack3 = [1,2]
        invalid_knapsack = [0,1,2]

        valid_knapsacks = [empty_knapsack, valid_knapsack1, valid_knapsack2, valid_knapsack3]
        possible_knapsacks = [[], valid_knapsack1, valid_knapsack2, valid_knapsack3, invalid_knapsack]
        assertListsEqual(self,
                         knapsack_problem.getAllValidKnapsackCombinations(possible_knapsacks, self.weights, self.capacity),
                         valid_knapsacks)


    def test_computeKnapsackWeight(self):
        knapsack = [0, 3, 6]
        weights = [10, 100, 100, 10, 100, 100, 10]

        self.assertEqual(knapsack_problem.computeKnapsackWeight(knapsack, weights), 30)


    def test_findMostValuableKnapsackCombinationsWithSingleMaximumValueKnapsack(self):
        knapsack_1 = [0, 1, 2]
        knapsack_2 = [0, 1, 3]
        highest_value_knapsack = [0, 1, 4]
        values = [1, 1, 1, 1, 5]

        assertListsEqual(
            self,
            knapsack_problem.findMostValuableKnapsackCombinations([knapsack_1, knapsack_2, highest_value_knapsack], values),
            [highest_value_knapsack])


    def test_findMostValuableKnapsackCombinationsWithMultipleMaximumValueKnapsack(self):
        knapsack_1 = [0, 1, 2]
        highest_value_knapsack = [0, 1, 3]
        highest_value_knapsack_2 = [0, 1, 4]
        values = [1, 1, 1, 5, 5]

        assertListsEqual(self,
                         knapsack_problem.findMostValuableKnapsackCombinations([knapsack_1, highest_value_knapsack, highest_value_knapsack_2], values),
                         [highest_value_knapsack, highest_value_knapsack_2])


    def test_computeKnapsackValue(self):
        knapsack = [0,3,6]
        values = [10,-10,-10,10,-10,-10,10]

        self.assertEqual(knapsack_problem.computeKnapsackValue(knapsack, values), 30)


    def test_findLightestKnapsackCombination(self):
        knapsack_1 = [0,2]
        knapsack_2 = [0,1]
        lightest_knapsack = [1,2]
        weights = [10, 5, 0]

        assertListsEqual(self,
                         knapsack_problem.findLightestKnapsackCombination([knapsack_1, knapsack_2, lightest_knapsack], weights),
                         lightest_knapsack)

    def test_validateDataWithValidData(self):
        weights = [1, 1, 1]
        values = [1, 1, 1]
        capacity = 10

        knapsack_problem.validateData(weights, values, capacity)

    def test_validateDataWithInvalidWeight(self):
        weights = [-1, 1, 1]
        values = [1, 1, 1]
        capacity = 10

        try:
            knapsack_problem.validateData(weights, values, capacity)
        except knapsack_problem.DataValidationError as validationError:
            self.assertEqual(validationError.getMessage(), "Data Error: All item weights must be non-negative numbers.")

    def test_validateDataWithInvalidValue(self):
        weights = [1, 1, 1]
        values = [-1, 1, 1]
        capacity = 10

        try:
            knapsack_problem.validateData(weights, values, capacity)
        except knapsack_problem.DataValidationError as validationError:
            self.assertEqual(validationError.getMessage(), "Data Error: All item values must be greater than or equal to 0.")

    def test_validateDataWithInvalidWeightCapacity(self):
        weights = [1, 1, 1]
        values = [1, 1, 1]
        capacity = -1

        try:
            knapsack_problem.validateData(weights, values, capacity)
        except knapsack_problem.DataValidationError as validationError:
            self.assertEqual(validationError.getMessage(), "Data Error: The weight capacity must be greater than or equal to 0.")


    def test_validateDataWithInvalidArrayLengths(self):
        weights = [1, 1, 1, 1]
        values = [1, 1, 1]
        capacity = -1

        try:
            knapsack_problem.validateData(weights, values, capacity)
        except knapsack_problem.DataValidationError as validationError:
            self.assertEqual(validationError.getMessage(), "Data Error: There is an unequal number of weights and values.")

    @patch("knapsack_problem.input", return_value="n")
    def test_promptForValidBooleanWithInputValueN(self, mock_input):
        result = knapsack_problem.promptForValidBoolean("test message")

        self.assertFalse(result)

    @patch("knapsack_problem.print")
    @patch('knapsack_problem.validateData')
    @patch('knapsack_problem.fillKnapsack')
    @patch('knapsack_problem.displayResults')
    @patch('knapsack_problem.promptForValidBoolean', return_value=False)
    def test_main(self,
                  mock_promptForValidBoolean,
                  mock_displayResults,
                  mock_fillKnapsack,
                  mock_validateData,
                  mock_print):

        knapsack_problem.main()

        mock_validateData.assert_called_once()
        mock_fillKnapsack.assert_called_once()
        mock_displayResults.assert_called_once()
        mock_promptForValidBoolean.assert_called_once()

if __name__ == "__main__":
    unittest.main()


## HELPER METHODS
def generatePointsInPlane():
    test_input = []
    for i in range(10):
        x = random.randrange(-100, 100)
        y = random.randrange(-100, 100)
        test_input.append((x, y))

    return test_input


def assertLineEquationLambdasEqual(context, line_equation_1, line_equation_2):
    test_input = generatePointsInPlane()

    for point in test_input:
        x_value = point[0]
        y_value = point[1]

        context.assertEqual(line_equation_1(x_value, y_value), line_equation_2(x_value, y_value))


def assertListsEqual(instance, list1, list2):
    instance.assertTrue(len(list1) == len(list2) and sorted(list1) == sorted(list2))
