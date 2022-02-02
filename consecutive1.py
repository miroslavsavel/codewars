def first_non_consecutive(arr):
    x = None
    for i, hodnota in enumerate(arr):
        if (i != len(arr) - 1):
            a = arr[i]
            b = arr[i+1]
            c = b-a
            if(c!=1):
                return arr[i+1]
    return x



pole = [1, 2, 7, 4, 6, 7]
a=first_non_consecutive(pole)
print(a)
