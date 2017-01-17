## Author:   Justice Adams
## Brute Force Robbers Knapsack Algorithm

## Consider a burglar who needs to steal the most valuable subset of items from a given location.
## This algorithm uses a list defining item weights, a list containing item values, and a knapsack capacity.
## Assume that weights[n] corresponds to values[n] (so weight at index n of the weights list represents item n and
## its corresponding value is values[n]. This script will find the most valuable combination of items that is
## possible to steal. I decided to leave out a user input feature, and instead, you must directly alter the data at
## the bottom of this file in order to change the input. The focus shouldn't be on UX, but rather the
## implementation...so I omitted it. Items are zero indexed.
##
## Note: If more than one knapsack combination yield the highest possible value, then the combination which yields
## the lowest weight will be chosen as it is considered optimal. If more than one combination both yield the highest
## value and have equal weight, only one combination is returned.

import itertools

MATPLOTLIB_INSTALLED = True
try:
    import matplotlib.pyplot as plt
except ImportError:
    MATPLOTLIB_INSTALLED = False


def fillKnapsack(weights, values, weight_capacity):
    """Takes in a list of item weights, a list of item values, and a knapsack capacity, then finds and returns
       the optimal combination of items that is possible to steal. If more than one combination both yeild the
       highest possible value, the lowest weighing combination is returned."""

    number_of_items = len(weights)
    
    power_set = computePowerset(range(number_of_items))

    valid_knapsacks = getAllValidKnapsackCombinations(power_set, weights, weight_capacity)

    most_valuable_knapsacks = findMostValuableKnapsackCombinations(valid_knapsacks, values)

    if len(most_valuable_knapsacks) > 1:
        most_valuable_knapsack = findLightestKnapsackCombination(most_valuable_knapsacks, weights)
    else:
        most_valuable_knapsack = most_valuable_knapsacks[0]

    return most_valuable_knapsack


def computePowerset(items):
    """Takes in a list of n items (represented as numbers [1,n]) and returns the powerset of all
       possible subsets of n items."""

    power_set = []
    for subset in powerset(items):
        power_set.append(subset)

    return power_set

    
def powerset(iterable):
    """As defined in Python Itertools documentation : https://docs.python.org/3/library/itertools.html#recipes
       powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def getAllValidKnapsackCombinations(possible_combinations, weights, weight_capacity):
    """Takes in all possible item combinations and a list of each items corresponding weights then returns a
       list containing only those combinations which are actually possible (they don't exceed the weight
       limit)."""
      
    valid_knapsacks = []
    for knapsack_combination in possible_combinations:
        if computeKnapsackWeight(knapsack_combination, weights) <= weight_capacity:
            valid_knapsacks.append(knapsack_combination)

    return valid_knapsacks


def computeKnapsackWeight(knapsack, weights):
    """Takes in a knapsack combination and a list of item weights. Returns the weight of the given knapsack
       combination."""
    
    total_weight = 0
    for item in knapsack:
        total_weight += weights[item]
    return total_weight


def findMostValuableKnapsackCombinations(valid_knapsacks, values):
    """Takes in a list of knapsack combinations and a list of item values then finds the most valuable
       combination (or combinations) and returns them in the form of a list."""
    
    max_value_combinations = []
    highest_value_knapsack = 0
    
    for knapsack_combination in valid_knapsacks:
        value_of_knapsack = computeKnapsackValue(knapsack_combination, values)

        if value_of_knapsack > highest_value_knapsack:
            max_value_combinations = [knapsack_combination]
            highest_value_knapsack = value_of_knapsack
        elif value_of_knapsack == highest_value_knapsack:
            max_value_combinations.append(knapsack_combination)

    return max_value_combinations


def computeKnapsackValue(knapsack, values):
    """Takes in a knapsack combination and a list of corresponding values. Returns the value of the given
       knapsack combination."""
    
    total_value = 0
    for item in knapsack:
        total_value += values[item]
    return total_value


def findLightestKnapsackCombination(knapsacks, weights):
    """Takes in a list of knapsack combinations and a list of each items weights. Returns the lightest knapsack of
       the given possible combinations (or one of them if there are more than one). Used to decide which knapsack
       configuration is best when there are multiple of equal worth."""

    lightest_knapsack = []
    lightest_knapsack_weight = None
    for knapsack_combination in knapsacks:
        knapsack_weight = computeKnapsackWeight(knapsack_combination, weights)
        if lightest_knapsack_weight == None or knapsack_weight < lightest_knapsack_weight:
           lightest_knapsack_weight = knapsack_weight
           lightest_knapsack = knapsack_combination

    return lightest_knapsack


def validateData(weights, values, weight_capacity):
    """Validates input data for the knapsack algorithm."""
    
    if not(len(weights) == len(values)):
        raise DataValidationError("Data Error: There is an unequal number of weights and values.")

    for weight in weights:
        if weight <= 0:
          raise DataValidationError("Data Error: All item weights must be non-negative numbers.")

    for value in values:
        if value < 0:
          raise DataValidationError("Data Error: All item values must be greater than or equal to 0.")

    if weight_capacity <=0:
        raise DataValidationError("Data Error: The weight capacity must be greater than or equal to 0.")


def displayResults(most_efficient_knapsack):
    """Displays the most efficient knapsack configuration to the user."""

    print("\n*Treating items as 0 indexed*")
    print("Most valuable knapsack includes items - " + str(most_efficient_knapsack))


def promptForValidBoolean(message):
    """Prompts the user to enter a valid boolean (y) or (n) for a given message. Will not accept a faulty answer."""
    
    while True:
        user_response = input("\n" + message + " (y)es or (n)o: ")
        if user_response.lower().strip() in ("y", "n"):
            user_response = (user_response == "y")
            break
        else:
            print("Invalid input. Enter (y)es or (n)o")

    return user_response


def displayKnapsackPieChart(knapsack, weights, values, capacity):
    """Displays pie chart of knapsack item weight distrobutions using external MatPlotLib library."""
    
    sizes = []
    labels = []
    for item in knapsack:
        sizes.append(weights[item]/capacity)
        labels.append("Item " + str(item) + ": value = $" + str(values[item]))
    
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Knapsack Pie Chart (percentages represent weight distribution)', bbox={'facecolor':'0.8', 'pad':5})
    plt.show()


def main():
    """Runs algorithm for the given data defined below. Prints the output and gives option to display a pie chart
       if MatPlotLib installed."""

    #Data values. Change Accordingly
    weights = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
    values = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
    capacity = 750
    
    print("Running Script...")
    validateData(weights, values, capacity)
    best_knapsack = fillKnapsack(weights, values, capacity)
    print("Done.")
    displayResults(best_knapsack)

    show_graphic = False
    if MATPLOTLIB_INSTALLED:
        show_graphic = promptForValidBoolean("Would you like to see a pie chart representing the knapsack?")

    if show_graphic:
        displayKnapsackPieChart(best_knapsack, weights, values, capacity)

if __name__ == '__main__':
    ##This keeps the script from running upon importing. Has to be explicitly excecuted.
    main()


class DataValidationError(RuntimeError):
    message = None

    def __init__(self, message):
        self.message = message
        super(RuntimeError, self).__init__(self, message)

    def getMessage(self):
        return self.message
