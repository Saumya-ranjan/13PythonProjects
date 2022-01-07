def leapyear():
    x = int(input("Enter the year to see if it is leap year or not:"))
    if (((x%4==0)and(x%100==0))or(x%400==0)):
        print(f"{x} is a leap year")
    else:
        print(f"{x} is not a leap year")


leapyear()
