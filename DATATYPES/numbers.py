fish = 22
print(fish, "is of type",type(fish))

fish = '22'
print(fish, 'is of type', type(fish))

weight = 5.05
print(weight,"is of type", type(weight))

#Data type 2. Python list
print("Print my list below: ")
mylist = ["Digikids", 458, 20, 74.93,"Students"]
print(mylist)

print("Extracting an item from the list")
print("mylist[1] list item is: ", mylist[1])
print("mylist[0] list item is: ", mylist[0])

#Show range
print("list range")
mylist = ["Digikids", 458, 20, 74.93,"Students",56,20,45,"pc",21]
print("mylist[2:6] is: ", mylist[2:6])
print("mylist[2:6] is: ", mylist[2:20])


print ("Print my list below: ")
mylist = ["Nathan", 14, 21, 7, 35, 69, 42, 78, 98, 49, 169]
print(mylist)
print("Extracting an item from the list")
print("mylist[1] list item is: ", mylist[4])
print("mylist[3] list item is: ", mylist[3])

#Show range
print("list range")
mylist = ["Nathan", 14, 21, 7, 35, 69, 42, 78, 98, 49, 169]
print("mylist[2:6] is: ", mylist[2:6])
print("mylist[2:6] is: ", mylist[2:20])

print("Print my list below: ")
mylist = ["Digikids", 458, 20, 74.93,"Students", ""]
mylist[0] = "Coder"
mylist[4] = "Visitor"
mylist[5] = 56
print(mylist)

#Data Type 3. Python Tuple
print("This are my tuples: ")
myvar = (14, 'digikids',4.5,"My Class", 57,6.7)
print('myvar[3] is:', myvar[3])
#myvar[1] =10

#Data Type 4. Python Strings
print("this are python strings: ")
greetings = "how are you?"
print(greetings)
hello = "how are you today? Will you go swimming in the afternoon?"
print(hello)
print(type(hello))
#Triple quotes
awesome = """
how are you?
Have you eaten?
Will you go swimming in the afternoon?
"""
print(awesome)
print(type(awesome))

good = "how are you?"
print("Extract good[2] is: ", good[5])
print(good[2:8])
print(type(good[2:8]))
# good[1]= 0



#Data Types 5. Python Set
print("print the ordered list")
books = {40, 32, 2,2,6,6,8,8,8,8,40,15,'digikids', 'digikids','Digikids' }
print(books)
print(type(books))

#Data Types 6. Python Dictionary
Digikids ={"student1":12, 'student2':8, 'student':15, 2:'parent'
}
print(Digikids[2])
print(type(Digikids[2]))

