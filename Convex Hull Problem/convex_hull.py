## Author:   Justice Adams
## Brute Force 2D Convex Hull Algorithm

## Given a set of points on the XY plane, this algorithm computes the convex
## hull that would contain all the points given. I decided to leave out a
## user input feature, and instead you must directly alter the array at the
## bottom of this file in order to change the input. The focus shouldn't be
## on UX, but rather the implementation... so I ommited it. Please keep
## floats under 10 digits to avoid floating point errors with specific
## geometric calculations.

## Note: this algoritm is set up such that if given a set of points that are
## all colinear, it will just return all points. Therefore it will let the line
## itslef be the convex hull.

print = print

MATPLOTLIB_INSTALLED = True
try:
    import matplotlib.pyplot as plt
except ImportError:
    MATPLOTLIB_INSTALLED = False

X_VAL = 0
Y_VAL = 1

def getPointsOfConvexHull(points_in_plane):
    """Takes in an array of tuples that represent a set of points in the XY plane, and returns an Array containing all points that make up
       the convex hull."""
    
    points_of_convex_hull = []
    n = len(points_in_plane)
    
    for i in range(0,n-1):
        pointI = points_in_plane[i]
        for j in range(i+1, n):
            pointJ = points_in_plane[j]
            
            if lineIsBorderOfHull(pointI, pointJ, points_in_plane):
                if MATPLOTLIB_INSTALLED:
                    prepareLineForPlot(pointI, pointJ)
                if pointI not in points_of_convex_hull:
                    points_of_convex_hull.append(pointI)
                if pointJ not in points_of_convex_hull:
                    points_of_convex_hull.append(pointJ)
                        
    return points_of_convex_hull


def prepareLineForPlot(point1, point2):
    """Takes in two points on the XY plane and uses the external library MatPlotLib to graph a green line between the two points"""
    
    plt.plot((point1[X_VAL], point2[X_VAL]), (point1[Y_VAL], point2[Y_VAL]), 'g-', lw=2)

    
def lineIsBorderOfHull(point1, point2, points_in_plane):
    """Takes in 2 points (tuples), constructs a line between them, and determines if the given line makes up one of the borders of the
       convex hull. If every other point lies on that line, this will return true."""
    
    line_equation = constructLineBetweenPoints(point1, point2)
    first_points_position_relative_to_line = None
    n = len(points_in_plane)

    for i in range(0,n):
        point = points_in_plane[i]

        if getPointsPositionRelativeToLine(point, line_equation) == 0:
            continue
        else:
            if first_points_position_relative_to_line == None:
                first_points_position_relative_to_line = getPointsPositionRelativeToLine(point, line_equation)
                continue

            if getPointsPositionRelativeToLine(point, line_equation) != first_points_position_relative_to_line:
                return False

    return True


def constructLineBetweenPoints(point1,point2):
    """Takes in 2 points (tuples) and returns a two variable function representing the line between those two points. Recognizes vertical
       lines and returns according function. Each equation set = 0 represents all points on said line."""
    
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


def getPointsPositionRelativeToLine(point, line_equation):
    """Takes in a 2 variable function representing the equation of a line and any point on the plane (Tuple), then determines that points
       location in relation to the given line. To avoid floating point error we round each result to 9 digits. See preface
       instructions."""

    equation_at_point = round(line_equation(point[X_VAL], point[Y_VAL]), 10)

    if equation_at_point > 0:
        return 1
    elif equation_at_point < 0:
        return -1
    else:
        return 0


def printPointsOfConvexHull(points_of_convex_hull):
    """Displays results by printing each point (ordered pair) making up the convex hull."""

    print("Script Over. Below are the following points that make up the convex hull:")

    for point in points_of_convex_hull:
        print("\t" + str(point))


def promptForValidBoolean(message):
    """Prompts the user to enter a valid boolean (y) or (n) for a given message. Will not accept a faulty answer."""
    
    while(True):
        user_response = input("\n" + message + " (y)es or (n)o: ")
        if user_response.lower().strip() in ("y", "n"):
            user_response = (user_response == "y")
            break
        else:
            print("Invlid input. Enter (y)es or (n)o")

    return user_response


def displayConvexHull(all_points_in_plane):
    """Displays convex hull scatter plot using external MatPlotLib library."""
    
    x_vals = []
    y_vals = []
    
    for point in (all_points_in_plane):
        x_vals.append(point[X_VAL])
        y_vals.append(point[Y_VAL])

    plt.scatter(x_vals,y_vals)
    plt.show()

def main():
    """Runs algorithm for the given set of points defined below. Prints the output and gives option to display graphic of convex hull."""

    ##Data set of points in plane. Change Accordingly.
    points_in_plane = [(-2,5), (1,1), (2,15), (30,30), (10,10), (15, 15), (30,1), (20,3), (25,10), (29, 2)]
    show_graphic = False
    
    points_of_convex_hull = getPointsOfConvexHull(points_in_plane)
    printPointsOfConvexHull(points_of_convex_hull)
    if MATPLOTLIB_INSTALLED:
        show_graphic = promptForValidBoolean("Would you like to see a graphic of the convex hull?")
    if show_graphic:
        displayConvexHull(points_in_plane)
    
if __name__ == '__main__':
    main()
