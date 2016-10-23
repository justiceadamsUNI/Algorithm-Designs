## Author:   Justice Adams
## Unit test for convex_hull script

## You must have installed the libraries mock
## (https://docs.python.org/dev/library/unittest.mock.html) as well
## as MatPlotLib (http://matplotlib.org/users/installing.html) for this
## test to be fully functional/exhaustive.

import unittest
from unittest import mock
import random
from mock import patch
import convex_hull


class TestConvexHull(unittest.TestCase):
    mSquareInPlane = [(0, 0), (0, 2), (2, 0), (2, 2)]
    mCollinearPointsInPlane = [(0, 0), (10, 10), (1, 1), (-1, -1)]
    mYEqualsX = staticmethod(lambda x, y: (x - 1) + 1 - y)
    X_VAL = 0
    Y_VAL = 1

    def setUp(self):
        print("Testing: ", self._testMethodName)


    def test_constructLineBetweenPointsWithNonVerticalLine(self):
        point1 = (1, 1)
        point2 = (5, 5)
        line = convex_hull.constructLineBetweenPoints(point1, point2)

        assertLineEquationLambdasEqual(self, line, self.mYEqualsX)


    def test_constructLineBetweenPointsWithVerticalLine(self):
        point1 = (1, 1)
        point2 = (1, 5)
        line = convex_hull.constructLineBetweenPoints(point1, point2)
        x_equals_1 = lambda x, y: x - 1

        assertLineEquationLambdasEqual(self, line, x_equals_1)


    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.scatter')
    def test_displayConvexHull(self, mock_scatter, mock_show):
        test_input = generatePointsInPlane()

        x_vals = []
        y_vals = []
        for point in test_input:
            x_vals.append(point[self.X_VAL])
            y_vals.append(point[self.Y_VAL])

        convex_hull.displayConvexHull(test_input)
        mock_scatter.assert_called_once_with(x_vals, y_vals)
        self.assertTrue(mock_show.called)


    def test_getPointsOfConvexHull(self):
        input_data = [self.mSquareInPlane[0], self.mSquareInPlane[1], self.mSquareInPlane[2], self.mSquareInPlane[3],
                      (1, 1), (1, 1.75)]

        assertListsEqual(self, self.mSquareInPlane, convex_hull.getPointsOfConvexHull(input_data))


    def test_getPointsOfConvexHullWithCollinearPoints(self):
        assertListsEqual(self, self.mCollinearPointsInPlane,
                         convex_hull.getPointsOfConvexHull(self.mCollinearPointsInPlane))


    def test_getPointsPositionRelativeToLineWithCollinearPoint(self):
        point = (10, 10)

        points_position_relative_to_line = convex_hull.getPointsPositionRelativeToLine(point, self.mYEqualsX)
        self.assertEqual(0, points_position_relative_to_line)


    def test_getPointsPositionRelativeToLineWithHigherPoint(self):
        point = (1, 10)

        points_position_relative_to_line = convex_hull.getPointsPositionRelativeToLine(point, self.mYEqualsX)
        self.assertEqual(-1, points_position_relative_to_line)


    def test_getPointsPositionRelativeToLineWithLowerPoint(self):
        point = (10, 1)

        points_position_relative_to_line = convex_hull.getPointsPositionRelativeToLine(point, self.mYEqualsX)
        self.assertEqual(1, points_position_relative_to_line)


    def test_lineIsBorderOfHullWithCollinearPoints(self):
        vector_tail = self.mCollinearPointsInPlane[0]
        vector_head = self.mCollinearPointsInPlane[1]

        self.assertTrue(convex_hull.lineIsBorderOfHull(vector_tail, vector_head, self.mCollinearPointsInPlane))


    def test_lineIsBorderOfHullWithInValidBorder(self):
        lower_left_corner = self.mSquareInPlane[0]
        upper_right_corner = self.mSquareInPlane[3]

        self.assertFalse(convex_hull.lineIsBorderOfHull(lower_left_corner, upper_right_corner, self.mSquareInPlane))


    def test_lineIsBorderOfHullWithValidBorder(self):
        lower_left_corner = self.mSquareInPlane[0]
        upper_left_corner = self.mSquareInPlane[1]

        self.assertTrue(convex_hull.lineIsBorderOfHull(lower_left_corner, upper_left_corner, self.mSquareInPlane))


    @patch("convex_hull.print", autospec=True)
    @patch("convex_hull.input", return_value="n")
    @patch('convex_hull.printPointsOfConvexHull')
    @patch('convex_hull.getPointsOfConvexHull')
    def test_main(self, mock_getPointsOfConvexHull, mock_printPointsOfConvexHull, mock_input, mock_print):
        convex_hull.main()

        self.assertTrue(mock_getPointsOfConvexHull.called)
        self.assertTrue(mock_printPointsOfConvexHull.called)


    @patch('matplotlib.pyplot.plot')
    def test_prepareLineForPlot(self, mock_plot):
        convex_hull.prepareLineForPlot((0, 0), (1, 1))
        mock_plot.assert_called_with((0, 1), (0, 1), 'g-', lw=2)


    @patch("convex_hull.print", autospec=True)
    def test_printPointsOfConvexHull(self, mock_print):
        test_input = generatePointsInPlane()
        convex_hull.printPointsOfConvexHull(test_input)

        calls = []
        for point in test_input:
            calls.append(mock.call("\t" + str(point)))

        mock_print.assert_has_calls(calls, any_order=False)


    @patch("convex_hull.input", return_value="n")
    def test_promptForValidBooleanWithInputValueN(self, mock_input):
        result = convex_hull.promptForValidBoolean("test message")

        self.assertFalse(result)


    @patch("convex_hull.input", return_value="y")
    def test_promptForValidBooleanWithInputValueY(self, mock_input):
        result = convex_hull.promptForValidBoolean("test message")

        self.assertTrue(result)


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


def assertListsEqual(context, list1, list2):
    context.assertTrue(len(list1) == len(list2) and sorted(list1) == sorted(list2))
