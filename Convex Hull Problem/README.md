# Convex Hull Problem

The convex hull algortithm was implemented in Python. According to [Wikipedia](https://en.wikipedia.org/wiki/Convex_hull) 
"In mathematics, the convex hull or convex envelope of a set X of points in the Euclidean plane or Euclidean space is the smallest
convex set that contains X." For more information on how the brute force algorith works, please see the comments within [convex_hull.py](convex_hull.py)
.The following algorithm was implemented for extra credit for CS 3530 Design and Analysis of Algorithms. 
I added unit test just for fun. Partly because I like to test code, and partly because I haven't explored unit test in python (untill now).

## MatPlotLib
In order to fully utilize the convex hull script I recommend installing [MatPlotLib](http://matplotlib.org/) to see a graphic of the
computed convex hull. You can install the MatPlotLib library quite easily with pip. 

`python -m pip install matplotlib`

## Mock
In order to run the test script [test_convex_hull.py](test_convex_hull.py) you should install [Mock](https://docs.python.org/3/library/unittest.mock.html)
so that the test can mock dependencies correctly. You can install the Mock library easily with pip.

`pip install -U mock`

## Example Script Run
Here's an gif of what it would look like to run the script with the following set of points: [(-2, 5), (1, -5), (2, 15), (30, 30), (10, 10), (15, 15), 
(30, -10), (20, 3), (25, 10), (29, 2),(-10, 10), (19, 19), (10, 9.8), (50, 45), (20, 67)]

Note that the gif is on a loop.

![output](http://imgur.com/5H4HhgV)
