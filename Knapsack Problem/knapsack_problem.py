## Author:   Justice Adams
## Brute Force Knapsack Solution Algorithm

## -- Insert info here when finished --

import itertools
import matplotlib.pyplot as plt

def fillKnapsack(weights, values, weight_capacity):
    number_of_items = len(weights)
    
    power_set = computePowerset(range(number_of_items))

    valid_knapsacks = getAllValidKnapsackCombinations(power_set, weights, weight_capacity)

    print(len(valid_knapsacks))

    most_valuable_knapsack = findMostValuableKnapsackCombination(valid_knapsacks, values)

    print("\n" + "most valuable knapsack includes items - " + str(most_valuable_knapsack))

    displayKnapsackPieChart(most_valuable_knapsack, weights, values, weight_capacity)


def computePowerset(items):
    """Takes in a list of n items (represented as numbers [1,n]) and returns the powerset of all
       possible subsets of n items"""

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
    """Takes in all possible item combinations and their corresponding weights then returns a list containing
       only those combinations which are actually possible (they don't exceeed the weight limit)"""
      
    valid_knapsacks = []
    for knapsack_combination in possible_combinations:
        if computeKnapsackWeight(knapsack_combination, weights) <= weight_capacity:
            valid_knapsacks.append(knapsack_combination)

    return valid_knapsacks


def computeKnapsackWeight(knapsack, weights):
    """Takes in a knapsack combination and a list of item weights. Returns the weight of the given knapsack
       combination"""
    
    total_weight = 0
    for item in knapsack:
        total_weight += weights[item]
    return total_weight


def findMostValuableKnapsackCombination(valid_knapsacks, values):
    """Takes in a list of knapsack combinations and a list of item values then finds the most valuable
       combination (only retuns one combination if there is more than one combination of equal worth)"""
    
    max_value_combination = []
    highest_value_knapsack = 0
    
    for knapsack_combination in valid_knapsacks:
        value_of_knapsack = computeKnapsackValue(knapsack_combination, values)
        if value_of_knapsack > highest_value_knapsack:
            max_value_combination = knapsack_combination
            highest_value_knapsack = value_of_knapsack

    return max_value_combination


def computeKnapsackValue(knapsack, values):
    """Takes in a list of items and list of corresponding values. Returns the value of the given knapsack
       combination"""
    
    total_value = 0
    for item in knapsack:
        total_value += values[item]
    return total_value


def displayKnapsackPieChart(knapsack, weights, values, capacity):
    """Displays pie chart of knapsack item weight distrobutions"""
    
    sizes = []
    labels = []
    for item in knapsack:
        sizes.append(weights[item]/capacity)
        labels.append("Item: " + str(item) + " value = " + str(values[item]))
    
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
    plt.show()


##weights = [382745,
##           799601,
##           909247,
##           729069,
##           467902,
##           44328,
##           34610,
##           698150,
##           823460,
##           903959,
##           853665,
##           551830,
##           610856,
##           670702,
##           488960,
##           951111,
##           323046,
##           446298,
##           931161,
##           31385,
##           496951,
##           264724,
##           224916,
##           169684]
##
##values = [ 825594,
##           1677009,
##           1676628,
##           1523970,
##           943972,
##           97426,
##           69666,
##           1296457,
##           1679693,
##           1902996,
##           1844992,
##           1049289,
##           1252836,
##           1319836,
##           953277,
##           2067538,
##           675367,
##           853655,
##           1826027,
##           65731,
##           901489,
##           577243,
##           466257,
##           369261]
##
##capacity  = 6404180


##weights = [382745,
##           799601,
##           909247,
##           729069,
##           467902,
##           44328,
##           34610,
##           698150,
##           823460,
##           903959,
##           853665,
##           551830,
##           610856,
##           670702,
##           488960,
##           951111,
##           323046,
##           446298,
##           931161,
##           31385,
##           496951,
##           264724,
##           224916,
##           169684]
##
##values = [ 825594,
##           1677009,
##           1676628,
##           1523970,
##           943972,
##           97426,
##           69666,
##           1296457,
##           1679693,
##           1902996,
##           1844992,
##           1049289,
##           1252836,
##           1319836,
##           953277,
##           2067538,
##           675367,
##           853655,
##           1826027,
##           65731,
##           901489,
##           577243,
##           466257,
##           369261]

weights = [ 70,73,77,80, 82,87,90,94,98,106,110,113,115,118,120]

values = [ 135,
139,
149,
150,
156,
163,
173,
184,
192,
201,
210,
214,
221,
229,
240]

capacity = 750



fillKnapsack(weights, values, capacity)
    

    
    


