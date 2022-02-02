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
        a = [i]
        b = [i+1]
        c = b-a
        c = 1
        if(c!=1):
            print([i+1])


                # print(hodnota)
    return x
pole = [1, 2, 3, 4, 6, 7]
# print(pole)
# print(pole[2])
# # k = pole[2]
# # l = pole[2+1]


first_non_consecutive(pole)
