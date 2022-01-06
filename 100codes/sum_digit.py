def sum_digit():
    x = input("Enter a Number: ")
    value = 0
    for z in x:
        value = value + int(z)
    print(f"The sum of this digit is {value}")

sum_digit()