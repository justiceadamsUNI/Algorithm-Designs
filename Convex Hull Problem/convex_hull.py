## Author:   Justice Adams
## Brute Force 2D Convex Hull Algorithm

## Given a set of points on the XY plane, this algorithm computes the convex
## hull that would contain all the points given. I decided to leave out a
## user input feature, and instead you must directly alter the array at the
## bottom of this file in order to change the input. The focus shouldn't be
## on UX, but rather the implementation... so I ommited it.

## Note: this algoritm is set up such that if given a set of points that are
## all colinear, it will just return all points. Therefore it will let the line
## itslef be the convex hull.

import matplotlib.pyplot as plt

X_VAL = 0
Y_VAL = 1

def get_points_of_convex_hull(points_in_plane):
    """Takes in an array of tuples that represent a set of points in the XY plane, and returns an Array containing all points that make up the convex
       hull."""
    
    points_of_convex_hull = []
    n = len(points_in_plane)
    
    for i in range(0,n-1):
        pointI = points_in_plane[i]
        for j in range(i+1, n):
            pointJ = points_in_plane[j]
            
            if line_is_border_of_hull(pointI, pointJ, points_in_plane):
                prepare_line_for_plot(pointI, pointJ)
                if pointI not in points_of_convex_hull:
                    points_of_convex_hull.append(pointI)
                if pointJ not in points_of_convex_hull:
                    points_of_convex_hull.append(pointJ)
                        
    return points_of_convex_hull


def prepare_line_for_plot(point1, point2):
    plt.plot((point1[X_VAL], point2[X_VAL]), (point1[Y_VAL], point2[Y_VAL]), 'g-', lw=2)

    
def line_is_border_of_hull(point1, point2, points_in_plane):
    """Takes in 2 points (tuples), constructs a line between them, and determines if the given line makes up one of the borders of the convex hull.
       If every other point lies on that line, this will return true."""
    
    line_equation = construct_line_between_points(point1, point2)
    first_points_position_relative_to_line = None
    n = len(points_in_plane)

    for i in range(0,n-1):
        point = points_in_plane[i]

        if get_points_position_relative_to_line(point, line_equation) == 0:
            continue
        else:
            if first_points_position_relative_to_line == None:
                first_points_position_relative_to_line = get_points_position_relative_to_line(point, line_equation)
                continue

            if get_points_position_relative_to_line(point, line_equation) != first_points_position_relative_to_line:
                return False

            
    return True


def construct_line_between_points(point1,point2):
    """Takes in 2 points (tuples) and returns a two variable function representing the line between those two points. Recognizes vertical lines and
       returns according function. Each equation set = 0 represents all points on said line."""
    
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


def get_points_position_relative_to_line(point, lineEquation):
    """Takes in a 2 variable function representing the equation of a line and any point on the plane (Tuple), then determines that points location in
       relation to the given line."""
    
    if lineEquation(point[X_VAL], point[Y_VAL]) > 0:
        return 1
    elif lineEquation(point[X_VAL], point[Y_VAL]) < 0:
        return -1
    else:
        return 0


def print_points_of_convex_hull(points_of_convex_hull):
    """Displays results by printing each point making up the convex hull in clockwise order."""

    print("Script Over. Below are the folloing points that make up the convex hull:")

    for point in points_of_convex_hull:
        print("\t" + str(point))


def prompt_for_valid_boolean(message):
    while(True):
        userResponse = input("\n" + message + " (y)es or (n)o: ")
        if userResponse.lower().strip() in ("y", "n"):
            userResponse = (userResponse == "y")
            break
        else:
            print("Invlid input. Enter (y)es or (n)o")

    return userResponse


def display_convex_hull(all_points_in_plane, points_of_convex_hull):
    x_vals = []
    y_vals = []
    
    for point in (all_points_in_plane):
        x_vals.append(point[X_VAL])
        y_vals.append(point[Y_VAL])

    plt.scatter(x_vals,y_vals)
    plt.show()
        

def main():
    """Runs algorithm for the given set of points defined below. Prints the output."""

    ##Data set of points in plane. Change Accordingly.
    points_in_plane = [(100, 0), (-100,0), (100,100), (-100, 100), (20,30), (30,40), (-50,50)]

    points_in_plane = [(1, 0), (1, 1), (1, -1), (0.68957, 0.283647), (0.909487, 0.644276), 
 (0.0361877, 0.803816), (0.583004, 0.91555), (-0.748169, 0.210483), 
 (-0.553528, -0.967036), (0.316709, -0.153861), (-0.79267, 0.585945),
 (-0.700164, -0.750994), (0.452273, -0.604434), (-0.79134, -0.249902), 
 (-0.594918, -0.397574), (-0.547371, -0.434041), (0.958132, -0.499614), 
 (0.039941, 0.0990732), (-0.891471, -0.464943), (0.513187, -0.457062), 
 (-0.930053, 0.60341), (0.656995, 0.854205)]
    
    points_of_convex_hull = get_points_of_convex_hull(points_in_plane)
    print_points_of_convex_hull(points_of_convex_hull)
    show_graphic = prompt_for_valid_boolean("Would you like to see a graphic of the convex hull?")

    if show_graphic:
        display_convex_hull(points_in_plane, points_of_convex_hull)
    

main()
