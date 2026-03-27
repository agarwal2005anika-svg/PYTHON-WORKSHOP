# #1.
# #list
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:] #colon is used to copy the list, so that if we change the value of one list, it will not affect the other list.
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)

# #2.
# def f(i, values =[]): #the values list is empty.
#     values.append(i) #values gets append/added into the list
#     print(values)

# f(1)
# f(2)
# f(3)

# #3.
# def func(value, values):
#     var =1
#     values[0] = 44
# t=3
# v = [1,2,3]
# func(t,v)
# print(t, v[0])

# #4.
# dict = {'c': 97, 'a': 96, 'b': 98}
# for _ in sorted(dict): #if no varible is used, then underscore is used as a placeholder.
#     print(dict[_])


# #5.
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1 #{'Apple': 1, 'Banana': 1, 'apple': 1} #the value of apple and Apple is different because of case sensitivity.}

# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))
# print(fruit)

# #6.
# #how to write an array in python
# arr = [1,2,3,4]

# for i in range(len(arr)):
#     if i==0:
#         print(arr[i+1]*arr[i+2]*arr[i+3])
#     elif i==1:
#         print(arr[i-1]*arr[i+1]*arr[i+2]) 
#     elif i==2:
#         print(arr[i-1]*arr[i-2]*arr[i+1])    
#     else:
#         print(arr[i-1]*arr[i-2]*arr[i-3])
