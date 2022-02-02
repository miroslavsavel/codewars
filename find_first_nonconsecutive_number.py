def main():
    print("Hello World!")

def druha():
    print("Druha!")

def tretia():
    print('tretia')

# x = 2
# if __name__ == "__main__":
#     druha()
#     tretia()
#     main()
#     list = [11, 12, 13, 14, 15, 16]
#     eva = [14, 15, 16, 17, 18, 19, 20, 21]
#     miro = [list, eva]
#     print(miro)
#     print(list)
#     x = len(eva)
#     print(x)
#

#if __name__ == "__main__":
    print('write 5 numbers')
    chlieviky = [0, 0, 0, 0, 0]


    # x = 0
    # for x in chlieviky:
    #     print(x)
    #     print('zadaj cislo')
    #     x = int(input())
    #     chlieviky[x] = x

    # Python3 code to iterate over a list
    # list = [1, 3, 5, 7, 9]
    #
    # # Using for loop
    # for i in chlieviky:
    #     print(i)

    list = [0,0,0,0,0]
    print('napis cisla')
    x = input()
    list = x.split()
    print(list)

    x = 0
    for x in list:
        x = int(x)

    print(list)