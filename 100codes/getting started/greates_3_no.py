def great():
    x = int(input("First Number: "))
    y = int(input("Second Number: "))
    z = int(input("Third Number: "))
    if(x>y and x>z):
        print(f"{x} is the Greatest Number")
    elif(y>x and y>z):
        print(f"{y} is the Greatest Number")
    elif(z>x and z>y):
        print(f"{z} is the Greatest Number")


great()