def palindrome(x):
    if x[-1::-1] == x:
        print(f"The word {x} is palindromic.")
    else:
        print("The word is Not palindromic")



y = input("Enter a string: ")
palindrome(y)