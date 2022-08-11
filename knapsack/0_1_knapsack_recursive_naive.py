


def knapSack(C,n, wt,val):
    if C == 0 or n == 0:
        return 0
    if wt[n-1] > C:
        # if the weight of item is greater than capacity of bag
        # we cannot take it, so we will call subproblem, we exclude it
        return knapSack(C, n-1, wt, val)
    else:
        # If we can take item into sack
        # there are two cases which we should compare
        # 1, if we take item into account
        # 2, or if we exclude it
        # we should return maximum from the values we can take
        return max( val[n-1] + knapSack(C-wt[n-1], n-1, wt, val),
                    knapSack(C, n-1, wt, val))


val = [10, 40, 50, 75]  # values for items
wt = [5, 10, 3, 12]     # weights for items
C = 20
n = len(val)
print(knapSack(C,n,wt,val))