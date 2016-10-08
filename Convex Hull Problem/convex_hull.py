## Author   Justice Adams
## Brute Force 2D Convex Hull Algorithm

## Given a set of points on the XY plane, this algorithm computes the convex
## hull that would contain all the points given. I decided to leave out a
## user input feature, and instead you must directly alter the array at the
## bottom of this file in order to change the input. The focus shouldn't be
## on UX, but rather the implementation... so I ommited it.

## Note: this algoritm is set up such that if given a set of points that are
## all colinear, it will just return all points. Therefore it will let the line
## itslef be the convex hull.


X_VAL = 0
Y_VAL = 1

def get_points_of_convex_hull(points_in_plane):
    """Takes in an array of tuples that represent a set of points, and returns an Array containing all points that make up the convex hull."""
    
    points_of_convex_hull = []
    n = len(points_in_plane)
    
    for i in range(0,n-1):
        pointI = points_in_plane[i]
        
        for j in range(i+1, n):
            pointJ = points_in_plane[j]
            
            if line_is_border_of_hull(pointI, pointJ, points_in_plane):
                    if pointI not in points_of_convex_hull:
                        points_of_convex_hull.append(pointI)
                    if pointJ not in points_of_convex_hull:
                        points_of_convex_hull.append(pointJ)
                        
    return points_of_convex_hull

def line_is_border_of_hull(point1, point2, points_in_plane):
    """Takes in 2 points (tuples), constructs a line between them, and determines if the given line makes up one of the borders of the convex hull.
       If every other point is on that line, this will returns true."""
    
    line_equation = construct_line_between_points(point1, point2)
    first_points_position_relative_to_line = None
    n = len(pointsInPlane)

    for i in range(0,n-1):
        point = points_in_plane[i]

        if points_position_relative_to_line(point, line_equation) == 0:
            continue
        else:
            if first_points_position_relative_to_line == None:
                first_points_position_relative_to_line = points_position_relative_to_line(point, line_equation)
                continue

            if points_position_relative_to_line(point, line_equation) != first_points_position_relative_to_line:
                return False


    print("Returning true for points: " + str(point1) + " " + str(point2))
    return True

def construct_line_between_points(point1,point2):
    """Takes in 2 points (tuples) and returns a function representing the line between those two points. Recognizes vertical lines and returns
       according function. Each equation set = 0 represents all points on said line."""
    
    point1_x = point1[X_VAL]
    point1_y = point1[Y_VAL]

    point2_x = point2[X_VAL]
    point2_y = point2[Y_VAL]

    delta_x = (point2_x - point1_x)

    if delta_x == 0:
        return lambda x, y: x - point2_x
    else:
        slope = (point2_y - point1_y)/(point2_x - point1_x)
        return lambda x, y: slope*(x - point1_x) + point1_y - y


def points_position_relative_to_line(point, lineEquation):
##    print("--------------------------------------------------")
##    print("line equation at point = " + str(point) + " - " + str(lineEquation(point[X_VAL], point[Y_VAL])))
    if lineEquation(point[X_VAL], point[Y_VAL]) > 0:
        return 1
    elif lineEquation(point[X_VAL], point[Y_VAL]) < 0:
        return -1
    else:
        return 0
    
            
def addPointsToArray(point1, point2, array):
    if point1 not in array:
        array.append(point1)
    if point2 not in array:
        array.append(point2)


pointsInPlane = [(0,0),
                 (2,2),
                 (0,2),
                 (2,0),
                 (1,1)]

testPointsInPlane =[(0,100),(100,100),(100,0),(0,0), (0,2), (50,2)]
                    

pointsInConvexHull = get_points_of_convex_hull(testPointsInPlane)

for point in pointsInConvexHull:
    print(point)
