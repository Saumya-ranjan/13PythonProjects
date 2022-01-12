def sumer():
    x = []
    y = int(input("Enter the array No.: "))
    target = int(input("Enter the target: "))
    for i in range(y):
        z = int(input("Enter the element: "))
        x.append(z)
    for k in x:
        for p in x:
            if k+p == target:
                print(x.index(k),x.index(p))
    
    
    
    
    
sumer()