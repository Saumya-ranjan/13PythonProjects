def fibonacci():
    x = int(input("Enter a Number to see fibonacci series till that Number: " ))
    n1 = 0
    n2 = 1
    temp = []
    for i in range (2,x+1):
        n3 = n1+n2
        n1 = n2
        n2 = n3
        temp.append(n3)
    print(temp)
        



fibonacci()