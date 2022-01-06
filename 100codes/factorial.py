def factorial():
    x = int(input("Enter a number to see factorial of: "))
    value = 1
    if x == 0:
        print(f"factorial of 0 is: 1")
    else:
        for i in range(1,x+1):
            value = value * i
        print(f"The factorial of {x} is: {value}")


factorial()