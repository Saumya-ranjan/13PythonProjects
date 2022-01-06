# def reverse():
#    num = int(input("Enter the Number:"))
#    temp = num
#    reverse = 0  
#    while num > 0:
#        remainder = num % 10
#        reverse = (reverse * 10) + remainder
#        num = num // 10
#    print("The Given number is {} and Reverse is {}".format(temp, reverse)) 
# reverse()


def reverse():
    num = input("Enter a word ")
    if (num[::-1] == num):
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not palindrome")

reverse()