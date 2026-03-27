#1.
# #list  
# myList = ["Vidhi", "Ashish", "komal", 77, 60.52, "sandip",]
# print(myList)
# print(type(myList))
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[-1]) #when we start indexing the list or array from last, its index starts from -1
# print(myList[2:5])
# print(myList[:5])
# print(myList[1:])
# print(myList[1:8:2])
# print(myList[:])
# print(myList[::-1])#reverses the array

#2.
# #operations on list
# myList = ["Vidhi", "Ashish", "komal", 77, 60.52, "sandip",]
# #to put value in last.
# myList.append('Harsh')
# myList.append("Laxman")
# print(myList)
# #to put value in perticular index
# myList.insert(1,"Sanket")
# print(myList)
# #to remove the elements
# myList.remove("sandip")
# print(myList)
# #to copy/clone the entire list
# newlist = myList.copy() #cloning
# print(myList)
# print(newlist)

#3.
# #nested list
# myList=[['Prashant','Jha'],['85.56'],[440022,"yyy"]]
# #overall structure of the list
# #       0         1
# # 0 [['Prashant','Jha']
# #1 ['85.56'],
# #2 [440022,     "yyy" ]] 

# print("Example of multidimensional list: ")
# print(myList) #print(myList[row][column])
# print(myList[0][0])
# print(myList[0][1])
# print(myList[1][0])
# print(myList[2][0])
# print(myList[2][1])


# 4. 
# #some more operations

# list1 = ["Vidhi", "Harde"]
# print(list1*2)

# list2 =[50, 25.50, 53, 23.0]
# print(list1+list2)
# del list2[1] #to delete an element from perticular index
# print(list2)
# list2.clear() #to delete entire list
# print(list2)


# 5. 
# name = "Vidhi"
# print(name)
# myname = list(name) #for typecasting
# print(myname)


# 6.
# #sorting
# mylist = [44,22,77,7,6,82]
# #ascending
# mylist.sort()
# print(mylist)
# #decending
# mylist.sort(reverse=True)
# print(mylist)


# 7. 
# #aliasing = assigning one variable reference to another.
# #if two variables(temperory) has same value, python's memory manager, the interpreter does not give seperate memory for it, it keeps the same memory address for them.
# math = 50
# phy = 50
# chem = 40
# print(id(math)) #id function is used to return the address of the variable
# print(id(phy))
# print(id(chem))

# #similar concept for lists
# mylist = [44,33,22,54,23,43]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))


# 8.
# #two types of special operators in python : membership, identity
# #membership operators : in, not in
# name = 'Vidhi'
# print('i' in name)
# print('i' not in name)

# #control statements 
# #loops
# #for loop
# #ascending order
# for i in range(1, 10, 2): #runs till 6, if 1 is not given the by default starts from 0. 2 is for incrementation, if 2 is not there, by default incrementation will be by 1.
#   print(i)

# #descending
# for i in range(5, 0, -1): 
#   print(i)

# #table
# for i in range(1,11):
#   print(i*2)


# 9. 
# #tables 
# for i in range(1,11):
#   print(i*2, " ", i*3, " ", i*4, " ", i*5, " ", i*6, " ", i*7, " ", i*8, " ", i*9, " ", i*10)
# for i in range(1,11):
#   print(i*11, " ", i*12, " ", i*13, " ", i*14, " ", i*15, " ", i*16, " ", i*17, " ", i*18, " ", i*19)


# 10.
# #conditions
# #if-else

# no = int(input("Enter any number: "))
# if no>0:
#   print("Positive")
# elif no<0:
#   print("Negative")
# else:
#   print("Zero")


# 11. 
# #program to accept the days and check if the day is working day or weekend.
# #normal logic
# # day= int(input("Enter to check the type of day (1-7 for Monday-Sunday): "))
# # if day<5:
# #   print("Its a working day")
# # else:
# #   print("Its a weekend")

# #good logic (logical operators)
# day= (input("Enter to check the type of day: "))
# if day=="Saturday" or day=="Sunday" or day=="saturday" or day=="sunday" or day=="SATURDAY" or day=="SUNDAY":
#   print("Its a weekend")
# else:
#   print("Its a working day")


# 12. 
# #to accept three papers marks and calculate total, percentage and if percentage is greater than or equal to 60 then eligible for placement.
# print("Enter student's marks for three subjects")
# sub1=int(input("Subject 1: "))
# sub2=int(input("Subject 2: "))
# sub3=int(input("Subject 3: "))

# total = sub1+sub2+sub3
# print("Total marks scored: ", total)
# percentage = total/3.0
# print("Percentage scored:", percentage)

# if percentage>=60:
#   print("Student is eligible for placement")
# else:
#   print("Student not eligible for placement")


# 13. 
# #accept five different values in five different variables and check the maximum value and print by using simple if statement

# print("Enter values below")
# v1 = int(input("Enter value1: "))
# v2 = int(input("Enter value2: "))
# v3 = int(input("Enter value3: "))
# v4 = int(input("Enter value4: "))
# v5 = int(input("Enter value5: "))

# if v1>v2 and v1>v3 and v1>v4 and v1>v5:
#   print("Value1 is maximum with value:", v1)
# elif v2>v1 and v2>v3 and v2>v4 and v2>v5:
#   print("Value2 is maximum with value:", v2)
# elif v3>v1 and v3>v2 and v3>v4 and v3>v5:
#   print("Value3 is maximum with value:", v3)
# elif v4>v1 and v4>v2 and v4>v3 and v4>v5:
#   print("Value4 is maximum with value:", v4)
# elif v5>v1 and v5>v2 and v5>v3 and v5>v4:
#   print("Value5 is maximum with value:", v5)
# else:
#   ("Some numbers are equal.")


