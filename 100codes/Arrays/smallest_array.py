def small():
    x = int(input("How many Number Do you want to enter: "))
    y=[]
    for i in range(x):
        z = int(input("enter the element: "))
        y.append(z)
    print(min(y))

small()


# size=int(input("ENTER ARRAY SIZE"))

# arr=[]

# for i in range(size):
#     element=int(input())
#     arr.append(element)

# print("SMALLEST ELEMENT",min(arr))