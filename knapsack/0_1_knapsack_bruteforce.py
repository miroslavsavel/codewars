# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapSack(C, n, wt, val):
    # Base Case
    if n == 0 or C == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n - 1] > C):
        return knapSack(C, n - 1, wt, val)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n - 1] + knapSack(C - wt[n - 1], n - 1, wt, val),
            knapSack(C, n - 1,wt, val))


# end of function knapSack


# Driver Code
val = [10, 40, 50, 75]  # values for items
wt = [5, 10, 3, 12]     # weights for items
C = 20                  # capacity of sack
n = len(val)            # number of items
print(knapSack(C, n, wt, val))

# This code is contributed by Nikhil Kumar Singh