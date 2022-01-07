def abundant():
    x = int(input("Enter a Number: "))
    temp = 0
    for i in range(1,x):
        if x % i == 0:
            temp = temp  + i
    if temp >= x:
        print(f"{x} is an abundant Number")
    else:
        print(f"{x} is Not an abundant Number")
            
            
    

abundant()
