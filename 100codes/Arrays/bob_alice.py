def alice():
    x=[]
    y=[]
    for f in range(3):
        a = int(input("Enter the alice score: "))
        b = int(input("Enter the bobs score: "))
        x.append(a)
        y.append(b)

    alice = 0
    bob = 0
    for k in range(3):
        if x[k]<y[k]:
            bob = bob+1
        elif x[k]>y[k]:
            alice=alice+1
        elif x[k]==y[k]:
            alice,bob
    print(alice,bob)     
    

    

alice()