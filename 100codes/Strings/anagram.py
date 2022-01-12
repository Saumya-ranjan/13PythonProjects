def anagram():
    x = input("Enter the String: ")
    y = input("Enter 2nd String: ")
    if len(x) == len(y):
        if sorted(x) == sorted(y):
            print(f"The string {x} and {y} are anagram")
        else:
            print(f"The string {x} and {y} are not anagram")
    else:
        print("The two strings are Different") 
        
        

anagram()