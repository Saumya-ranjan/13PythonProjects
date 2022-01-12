def nonrepeat():
    x = input("Enter a string: ")
    for i in x:
        value = 0
        for j in x:
            if i == j:
                value = value + 1
            elif value > 1:
                break
        if value == 1:
            print(i)

        


nonrepeat()