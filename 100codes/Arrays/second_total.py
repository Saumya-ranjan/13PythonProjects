def total():
    arr=[]
    x = int(input("Enter the No. of array: "))
    for i in range(x):
        y = int(input("Enter the Numbers:"))
        arr.append(y)
    arr.sort()
    if (arr[-1] == arr[-2]):
        print(arr[-3])
    elif(arr[-1]==arr[-2]==arr[-3]):
        print(arr[-4])
    else:
        print(arr[-2])
    
    
    


total()