def remove():
    x =input("Enter the string: ")
    value = 0
    for i in x:
        if i.isnumeric():
            value = value + int(i)

    print(f"The sum of given text {x} is {value}")

    
remove()


# first and last letter of string to uppercase:

# def first():
#     x = input("Enter a string: ")
#     y = len(x)
#     if x[0].islower():
#         x = x.replace(x[0],x[0].upper())
#         if x[y-1].islower():
#             x = x.replace(x[y-1],x[y-1].upper())
#     print(x)
    

# first()