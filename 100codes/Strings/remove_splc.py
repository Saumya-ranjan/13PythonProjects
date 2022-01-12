def remove():
    x = input("Enter a String: ")
    value = ""
    for i in x:
        if i.isalpha():
            value = value + i
    print(f"The Removed charater of {x} is: {value}")


remove()




# Removing white spaces

# def remove():
#     x = input("Enter a string: ")
#     value=x
#     for i in x:
#         if i.isspace():
#             value = value.replace(" ","")
#     print(f"the removed value of {x} is: {value} ")


# remove()
