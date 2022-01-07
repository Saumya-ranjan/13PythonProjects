def strlenr():
    value = 0
    x = input("Enter the character: ")
    # print(len(x))
    for i in x:
        value = value + 1
    print(f"{x} is of {value} length.")



strlenr()