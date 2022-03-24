number = int(input(" Enter an integer: "))
if((number%5==0)and(number%7==0)):
    print(number, "is a multiple of both 5 and 7")
else:
    print(number, "is not a multiple of 5 and 7")