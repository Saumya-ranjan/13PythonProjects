def rotate():
    arr =[]
    x = int(input("Enter the Number of array: "))
    z = int(input("Enter the element by which u want to rotate array: "))
    for i in range(x):
        y = input("Enter the values: ")
        arr.append(y)
    for k in range(z):
        arr.remove(arr[k])
    print(arr)
        

    



rotate()