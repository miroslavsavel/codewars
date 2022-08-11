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
    print(items)


# test greedy
greedy_knapsack(items, 2000)