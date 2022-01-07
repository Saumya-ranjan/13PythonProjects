def armstrong():
    x = input("Enter a Number to see if its a armstrong Number or Not: ")
    value = 0
    for i in x:
        value = value + (int(i)*int(i)*int(i))
        if value == int(x):
            print("Its an armstrong Number",value)
            break
    else:
        print("Its not an armstrong")
        


armstrong()