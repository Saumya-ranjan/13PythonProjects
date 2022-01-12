def sec():
    x = int(input("How many elements do u want to enter: "))
    y = []
    for i in range(x):
        z = int(input("Enter the elements: "))
        y.append(z)
    y.sort()
    print(y[1])
    


sec()