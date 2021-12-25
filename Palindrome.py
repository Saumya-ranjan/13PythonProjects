def palindrome(word):
    for x in range(0,int(len(word)/2)):
        if word[x] != word[len(word)-x-1]:
            return False
    return True
            


s = input("enter the word: ")
ans = palindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")
  