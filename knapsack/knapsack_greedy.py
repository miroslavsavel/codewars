items = [
            ('avocado', 2.2, 170),
            ('pomelo', 8, 1500),
            ('durian', 22, 1500),
            ('cucamelon',0.26, 15),
            ('lychee', 0.4, 20),
            ('star apple', 1, 200)
        ]

def greedy_knapsack(items, capacity):
    # find the fruit with the highest profit
    # first we sort the list by key for value using lambda
    items = sorted(items,key=lambda item:item[1], reverse=True)     #??check for lambdas
    # print(items)
    chosen_fruits = {}
    profit = 0
    for i in range(len(items)):
        # for each fruit in sorted array
        # 1. we want know how much of this fruit shoudl can we add to the bag, how many times the fruit can we put in the bag
        # 2. and how much capacity left
        name, value, weight = items[i]    #tupple unpacking
        # how many fruits of this type can we take
        num_of_fruit = (capacity - capacity % weight) / weight
        chosen_fruits[name] = num_of_fruit
        capacity = capacity % weight
        profit += num_of_fruit * value
    return round(profit,2), chosen_fruits

"""
slightly better performance
"""
def greedy_knapsack_dantzig(items, capacity):
    # find the fruit with the highest profit
    # first we sort the list by key for value using lambda
    items = sorted(items,key=lambda item:item[1]/item[2], reverse=True)     #??check for lambdas
    # print(items)
    chosen_fruits = {}
    profit = 0
    for i in range(len(items)):
        # for each fruit in sorted array
        # 1. we want know how much of this fruit shoudl can we add to the bag, how many times the fruit can we put in the bag
        # 2. and how much capacity left
        name, value, weight = items[i]    #tupple unpacking
        # how many fruits of this type can we take
        num_of_fruit = (capacity - capacity % weight) / weight
        chosen_fruits[name] = num_of_fruit
        capacity = capacity % weight
        profit += num_of_fruit * value
    return round(profit,2), chosen_fruits
# test greedy ! this ist optimal solution
print(greedy_knapsack(items, 2000))
print(greedy_knapsack_dantzig(items, 2000))