def vowels():
    x = input("User Enter a String: ").lower()
    value = 0
    for i in x:
        if (i == 'a' or i=="e" or i=="i" or i=="u" or i =="o" ):
            value = value+1
    print(f"The count of vowels in this sentence is: {value}")



vowels()


# Removing vowels from the string

# def remove():
#     x = input("Enter a string: ")
#     value=""
#     for i in x:
#         value=value+i
#         if(i == 'a' or i=="e" or i=="i" or i=="u" or i =="o" ):
#             value=value.replace(i,"")
#     print(f"The list without vowels are: {value}")

            


# remove()