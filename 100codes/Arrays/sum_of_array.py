def sume():      #Dont use sum as function ever use different name always.
    x = int(input("Enter the No. of array u want to put: "))
    numbers = []
    value=0
    for i in range(x):
        y = int(input("Enter the Numbers: "))
        numbers.append(y)
    print(sum(numbers))
    
    
    
sume()

