def grades():
    arr = []
 
    x = int(input("Enter the nUmber of array: "))
    for i in range(x):
        y = int(input("Enter the Elements of array: "))
        arr.append(y)

    for k in arr:
        if k <  38:
            print(k)
        elif k%5 < 3:
            while k%5 != 0:
                k+=1
        print(k)


grades()