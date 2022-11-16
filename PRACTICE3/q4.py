# Q4). Write a program in Python for, How to compare two array is equal in size or not.
n=int(input("Enter the size:-"))
a=[]
for i in range(n):
    num=int(input("Enter the number you want to enter:-"))
    a.append(num)
n1=int(input("Enter the size:-"))
b=[]
for i in range(n1):
    num1=int(input("Enter the number you want to enter:-"))
    b.append(num1)
if n==n1:
    print("They are of equal size")
else:
    print("They are of different size")