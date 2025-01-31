#Write a Program to check if two numbers are equal without using any comparison operator.

num1=int(input("enter first number"))
num2=int(input("Enter Second Number"))

if ((num1^num2)!=0):
    print("{} and {}  are not equal".format(num1,num2))
else:
   print("{} and {} are equal". format(num1,num2))


