# #1. 
# #types
# math = 40
# pi = 3.14
# name = 'Vidhi Harde'
# print(type(math))
# print(type(pi))
# print(type(name))

# #2.
# #input function by default only takes inputs as string.
# val1 = int(input("Enter value 1: "))
# val2 = int(input("Enter value 2: "))
# print(val1+val2)

# #3. 
# #integer typecasting
# #every datatype can be type cast in integer except imaginary numbers and combination of string and floats.
# print(int(3.14))
# print(int(True))
# print(int(False))
# print(int("4"))
# #print(int("Vidhi"))
# #print(int(3+4j))

# #4. 
# #float typecasting
# #every datatype can be type cast in float except imaginary numbers and combination of string and floats.

# print(float(3))
# print(float(True))
# print(float(False))
# print(float("4"))
# #print(float("Vidhi"))
# #print(float(4+7j))

# #5. 
# #complex typecast
# #every datatype can be type cast in complex except strings.

# print(complex(3))
# print(complex(4.5))
# print(complex(True))
# print(complex(False))
# print(complex(True,False))
# print(complex("4"))
# #print(complex("Vidhi"))
# print(complex(4+7j))
# print(complex(5,-3))


# #6.
# #boolean typecasting
# #false when 0 value is provided in any datatype else 1 always.
# print(bool(0))
# print(bool(4))
# print(bool(4.5))
# print(bool(0.0))
# print(bool(1+2))
# print(bool(True))
# print(bool(False))
# print(bool("4"))
# print(bool("Vidhi"))
# print(bool(0+0j))
# print(bool(-3))

# #7. 
# #simple interest
# principal = 100000
# roi = 10
# time = 1
# si = principal*roi*time/100
# print(si)

# #8. 
# #accept the temperature in celsius and convert in into fahrenheit
# celsius = float(input("Enter the temperature in degree celsius: "))
# fahrenheit = celsius* 9/5 + 32
# print("The temperature in fahrenheit is ", fahrenheit)

# #9.
# #swapping
# val1 = int(input("Enter value 1: "))
# val2 = int(input("Enter value 2: "))

# print("Before swapping")
# print("Value 1 is :", val1)
# print("Value 2 is :", val2)

# #using temp variable
# # temp = val1
# # val1 = val2
# # val2 = temp

# #without using temp variable to tackle the space complexity issue: suppose val1 =100, val2=200
# val1 = val1+val2   #100+200 = 300 = val1
# val2=val1-val2     #300-200 = 100 = val2
# val1=val1-val2     #300-100 = 200 = val1

# print("After swapping")
# print("Value 1 is :", val1)
# print("Value 2 is :", val2)

# #10.
# #convert height in feet into inches and cms
# feet = float(input("Enter height in feet: "))
# inch = feet*12
# cm = inch*2.54
# print("Height in inches:", inch)
# print("Heigh in cms:", cm)

# #11.
# #reversing a number
# num = 123
# print(num)
# a = num % 10 #3
# num = num // 10 #num = 12 , removed 3
# b = num % 10 #2
# num2 = num // 10 #num = 1 , removed 2
# rev = a*100 + b*10 + num2*1 #300+200+1
# print(rev)

# #12.
# num = 1234567 # The number to be reversed
# reversed_num = 0

# while num > 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num = num // 10

# print("The reversed number is:", reversed_num)