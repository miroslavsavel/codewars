items = [
            ('avocado', 2.2, 170),
            ('pomelo', 8, 1500),
            ('durian', 22, 1500),
            ('cucamelon',0.26, 15),
            ('lychee', 0.4, 20),
            ('star apple', 1, 200)
        ]

def dynamic_fruit(items, capacity):
    bag = [0 for i in range(capacity+1)]    # this will put capacity+1 zeroes to the list
    for i in range(capacity+1):
        for j in range(len(items)):
            # we have check for all possible pieces of fruit
            _, value, weight = items[j]     # unpack the  tupple
            # check if the weight of fruit if less than current capacity ( semi cpacity that will be growing
            if(weight < i):
                # check which of these two things is best solution
                # bag[i] is bag without specific fruit in
                # and the value of fruit within bag bag[i-weight] + value
                bag[i] = max(bag[i], bag[i-weight] + value)
    return round(bag[capacity])


# test greedy ! this ist optimal solution
print(dynamic_fruit(items, 2000))