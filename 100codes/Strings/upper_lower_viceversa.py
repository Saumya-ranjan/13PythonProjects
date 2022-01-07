def upper_lower():
    x = input("Enter a string: ")
    temp = ""
    for i in x:
        if i.islower():
            i = i.upper()
            temp = temp + i
        elif i.isupper():
            i = i.lower()
            temp = temp + i
    print(temp)

upper_lower()



# Tuple is not writable so u cant edit it 
# but we can say that x = "" and then use it 
# for list use x=[] and we can append it