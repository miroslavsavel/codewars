def first_non_consecutive(arr):
    #your code here
    x = None
    # for i in arr:
    #     if(i!=i+1):
    #         print(i+1)
    for i, hodnota in enumerate(arr):
        # print(i, hodnota)
        # if(i!=len(arr)-1):
        #     if(arr[i]<arr[i+2]):
        if (i != len(arr) - 1):
            a = arr[i]
            b = arr[i+1]
            c = b-a
            if(c!=1):
                #print(arr[i+1])
                return arr[i+1]


                # print(hodnota)
    return x
pole = [1, 2, 7, 4, 6, 7]

a=first_non_consecutive(pole)
print(a)
