def factors():
    x = int(input("Enter the Number to see factors of: "))
    temp =[]
    for i in range (1,x+1):
        if x % i == 0:
            temp.append(i)
    print(temp)


factors()