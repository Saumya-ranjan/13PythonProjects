def prime():
    x = int(input("enter a number:"))
    if x >= 1:
        for i in range(2,x):
            if (x % i == 0):
                print(f"{x} is not a prime Number")
                break
        else:
            print("its a prime number")


    elif(x == 0):
        print("Its zero")
    else:
        print(f"Negative Number")
prime()