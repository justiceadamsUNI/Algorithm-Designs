## Author:   Justice Adams
## Brute Force Knapsack Solution Algorithm

## -- Insert info here when finished --

import itertools


def fillKnapsack(weights, values, weight_limit):
    number_of_items = len(weights)
    
    power_set = computePowerSet(range(number_of_items))

    valid_knapsacks = getAllValidKnapsackCombinations(power_set, weights, weight_limit)

    print(valid_knapsacks)

    most_valuable_knapsack = findMostValuableCombination(valid_knapsacks, values)

    print(most_valuable_knapsack)


def findMostValuableCombination(valid_knapsacks, values):
    max_value_combination = []
    max_value = 0
    
    for knapsack_combination in valid_knapsacks:
        value_of_knapsack = 0
        for item in knapsack_combination:
            value_of_knapsack += values[item]

        if value_of_knapsack < max_value:
            max_value_combination = knapsack_combination

    return max_value_combination
        
        

def getAllValidKnapsackCombinations(possible_combinations, weights, weight_limit):
    valid_knapsacks = []

    for knapsack_combination in possible_combinations:
        total_weight = 0
        for item in knapsack_combination:
            total_weight += weights[0]
        if total_weight <= weight_limit:
            valid_knapsacks.append(knapsack_combination)

    return valid_knapsacks


def computePowerSet(items):
    power_set = []
    
    for subset in powerset(items):
        power_set.append(subset)

    return power_set
    
        

    


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


fillKnapsack([10,20,30], [10,20,30], 40)
    

    
    


