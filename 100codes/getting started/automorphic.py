def automorphic():
    n=int(input("Enter any number: "))
    x=n**2
    a=str(n)
    b=str(x)
    y=len(a)
    z=len(b)
    if(z-b.find(a)==y):
        print("Automorphic")
    else:
        print("Not automorphic number")
    
   
        



automorphic()