# CS DOJO
# https://www.youtube.com/watch?v=xOlhR_2QCXY
# very slow solution
w = [0, 1, 2, 4, 2, 5]      #the first zero in both arrays is dummy var
v = [0, 5, 3, 5, 3, 2]
n = 5
C = 10


# classic naive recursive solution
def KS(n,C):
    if (n == 0 or C == 0):
        result = 0
    elif w[n] > C:
        # we can't put it in the bag
        result = KS(n-1, C)
    else:
        tmp1 = KS(n-1, C)
        tmp2 = v[n] + KS(n-1, C - w[n])
        result = max(tmp1, tmp2)
    return result

# dynamic programming solution
# initialize arr[n][C] = undefined
# https://stackoverflow.com/questions/65401611/creating-a-2d-array-with-all-elements-initially-set-to-none
arr = [[None for j in range(n)] for i in range(C)]
def dyn_KS(n, C):
    if (arr[n][C] != None):
        return arr[n][C]
    if (n == 0 or C == 0):
        result = 0
    elif w[n] > C:
        # we can't put it in the bag
        result = KS(n-1, C)
    else:
        tmp1 = KS(n-1, C)
        tmp2 = v[n] + KS(n-1, C - w[n])
        result = max(tmp1, tmp2)
    arr[n][C] = result
    return result

print(KS(n,C))
print(dyn_KS(n,C))