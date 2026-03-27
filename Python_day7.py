# #1.
# import re
# var = 'gasgg54@#vscsd!s*'
# count = 0
# for i in var:
#     #z = re.findall('[a-z,0-9]',i)
#     z = ord(i)
#     #print(z)
#     if z>=97 and z<=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count+=1
# print(count)

# #2.
# #to check which number is present in all the three arrays
# a = [1,3,2]
# b = [2,3,4]
# c = [3,4,5]
# for i in a:
#     if i in b and i in c: #checks all the lists just by this function, 
#         print(i)

# #3.
# # to take all the zeroes and put them in last.
# mylist = [0,1,0,3,12]
# for i in mylist:
#     if i in mylist:
#         if i == 0:
#             mylist.remove(i)
#             mylist.append(i)

# print(mylist)

# #4.
# #to find second largest number
# list = [3,7,8,6,9,4,10]
# list.sort()
# print(list)
# print(list[-2])

#5.
#find the total distance between adjacent terms of list of 5 numbers.
N = int(input())
sum = 0
myList = []
for i in range(N):
    a = int(input("Enter element value: "))
    myList.append(a)
for j in range(len(myList)):
    if j+1 in range(len(myList)):
        sum+=abs(myList[j]-myList[j+1])
print(sum)        