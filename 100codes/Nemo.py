def Nemo():
    arr = ['wwe','wwr','rfaf','dafae','nemo','wafea','faefg','afeaf']
    for i in arr:
        if i=='nemo':
            print("Found Nemo")
            break
        else:
            print("running")

Nemo()

# But what if Nemo is at last so if we talk about 
# Big O then we always talk about Worst Case.

def Nemo():
    arr = ['wwe','wwr','rfaf','dafae','wafea','faefg','afeaf','nemo']
    for i in arr:
        if i=='nemo':
            print("Found Nemo")
            break
        else:
            print("running")

Nemo()