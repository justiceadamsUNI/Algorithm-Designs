import unittest
from mock import patch
import convex_hull as convex_hull



class TestConvexHull(unittest.TestCase):

    def setUp(self):
        print("\nTesting: ", self._testMethodName, end = " Status: -> ")     


    @patch('matplotlib.pyplot.plot')
    def test_prepareLineForPlot(self, mock):
        convex_hull.prepareLineForPlot((0,0), (1,1))
        self.assertTrue(mock.called)


    def test_LineIsBorderOfHullWithValidBorder(self):
        corner1 = (0,0)
        corner2 = (0,2)
        corner3 = (2,2)
        corner4 = (2,0)
        square_in_plane = [corner1, corner2, corner3, corner4]

        self.assertTrue(convex_hull.lineIsBorderOfHull(corner1, corner2, square_in_plane))


    def test_LineIsBorderOfHullWithInValidBorder(self):
        corner1 = (0,0)
        corner2 = (0,2)
        corner3 = (2,2)
        corner4 = (2,0)
        square_in_plane = [corner1, corner2, corner3, corner4]

        self.assertFalse(convex_hull.lineIsBorderOfHull(corner1, corner3, square_in_plane))


    def test_LineIsBorderOfHullWithColinearPoints(self):
        vector_tail = (0,0)
        vector_head = (10,10)
        point_1_on_line = (1,1)
        point_2_on_line = (-1,1)
        
        colinear_points = [vector_tail, vector_head, point_1_on_line, point_2_on_line]

        self.assertTrue(convex_hull.lineIsBorderOfHull(vector_tail, vector_head, colinear_points))
        
        



if __name__ == "__main__":
    unittest.main()
