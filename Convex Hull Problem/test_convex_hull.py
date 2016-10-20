import unittest
import random
from mock import patch
import convex_hull as convex_hull



class TestConvexHull(unittest.TestCase):

    def setUp(self):
        print("\nTesting: ", self._testMethodName, end = " Status: -> ")     


    @patch('matplotlib.pyplot.plot')
    def test_prepareLineForPlot(self, mock):
        convex_hull.prepareLineForPlot((0,0), (1,1))
        self.assertTrue(mock.called)


    def test_lineIsBorderOfHullWithValidBorder(self):
        corner1 = (0,0)
        corner2 = (0,2)
        corner3 = (2,2)
        corner4 = (2,0)
        square_in_plane = [corner1, corner2, corner3, corner4]

        self.assertTrue(convex_hull.lineIsBorderOfHull(corner1, corner2, square_in_plane))


    def test_lineIsBorderOfHullWithInValidBorder(self):
        corner1 = (0,0)
        corner2 = (0,2)
        corner3 = (2,2)
        corner4 = (2,0)
        square_in_plane = [corner1, corner2, corner3, corner4]

        self.assertFalse(convex_hull.lineIsBorderOfHull(corner1, corner3, square_in_plane))


    def test_lineIsBorderOfHullWithColinearPoints(self):
        vector_tail = (0,0)
        vector_head = (10,10)
        point_1_on_line = (1,1)
        point_2_on_line = (-1,1)
        
        colinear_points = [vector_tail, vector_head, point_1_on_line, point_2_on_line]

        self.assertTrue(convex_hull.lineIsBorderOfHull(vector_tail, vector_head, colinear_points))
        

    def test_constructLineBetweenPointsWithNonVerticalLine(self):
        point1 = (1,1)
        point2 = (5,5)
        line = convex_hull.constructLineBetweenPoints(point1, point2)
        y_equals_x = lambda x, y: (x - point1[0]) + point1[1] - y

        test_input = generateTestInput()

        for test_point in test_input:
           test_x = test_point[0]
           test_y = test_point[1]
            
           self.assertEqual(line(test_x, test_y), y_equals_x(test_x, test_y))


    def test_constructLineBetweenPointsWithVerticalLine(self):
        point1 = (1,1)
        point2 = (1,5)
        line = convex_hull.constructLineBetweenPoints(point1, point2)
        vertical_line = lambda x, y: x - point2[0]

        test_input = generateTestInput()

        for test_point in test_input:
           test_x = test_point[0]
           test_y = test_point[1]
            
           self.assertEqual(line(test_x, test_y), vertical_line(test_x, test_y))
           

    def test_getPointsPositionRelativeToLineWithHigherPoint(self):
        y_equals_x = lambda x, y: (x - 1) + 1 - y
        point = (1,10)

        points_position_relative_to_line = convex_hull.getPointsPositionRelativeToLine(point, y_equals_x)
        self.assertEqual(-1, points_position_relative_to_line)


    def test_getPointsPositionRelativeToLineWithLowerPoint(self):
        y_equals_x = lambda x, y: (x - 1) + 1 - y
        point = (10,1)

        points_position_relative_to_line = convex_hull.getPointsPositionRelativeToLine(point, y_equals_x)
        self.assertEqual(1, points_position_relative_to_line)


    def test_getPointsPositionRelativeToLineWithColinearPoint(self):
        y_equals_x = lambda x, y: (x - 1) + 1 - y
        point = (10,10)

        points_position_relative_to_line = convex_hull.getPointsPositionRelativeToLine(point, y_equals_x)
        self.assertEqual(0, points_position_relative_to_line)


    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.scatter')
    def test_displayConvexHull(self, mock_scatter, mock_show):
        test_input = generateTestInput()

        x_vals = []
        y_vals = []
        for point in test_input:
            x_vals.append(point[0])
            y_vals.append(point[1])

        convex_hull.displayConvexHull(test_input)
        mock_scatter.assert_called_once_with(x_vals, y_vals)
        self.assertTrue(mock_show.called)
            
        
        
        

## HELPER METHODS
def generateTestInput(): ##Change name of method
    test_input = []
    for i in range(10):
        x = random.randrange(-100, 100)
        y = random.randrange(-100, 100)
        test_input.append((x,y))

    return test_input
        

if __name__ == "__main__":
    unittest.main()
