#While loop example
value =  1
while value < 8:
    print(value)
    value = value + 1

#The never-ending loop. Infinite While loop
#while True:
    #print("ur mum")

#Break statement in python
print("\nShow how to break statement")
value = 4999
while value < 1000000:
        print(value)
        if value == 5000:
            break
        value = value + 1

#continued statement
print("\nShow continued statement")
values = 2
while values < 8:
    values = values + 1
    if values ==5:
        continue
    print(values)

#whileloop in multiple conditions
value1 = 10 
value2 = 20
while value1 > 0 and value2 > 0:
    print((value1, value2))
    value1 = value1 -3
    value2 = value2 -5

#While loop with else statement
print("\nShow while loop with else statement")
count = 0
while count < 4:
    print("My count is less than 4")
    count = count + 1
else:
    print("My count is not less than 4")

#Reversing using while loop
print("\nShow reversing using while loop in python")
my_list = ["welcome", "to", "Python3", "programming"]
r = len(my_list) - 1
while r >= 0:
    print(my_list[r])
    r = r - 1

#While else
print("\nWhile Else")
num = 3
while num > 0:
    num = num - 1
    print(num)
else:
    print("The end of loop")
