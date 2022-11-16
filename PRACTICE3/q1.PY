# Q1). Write a program in Python for, In array 1-100 numbers are stored,
#  one number is missing how do you find it.
a=[],s=0
n=int(input("Enter the number of size:-"))
for i in range(n-1):
    num=int(input("Enter the number:-"))
    s+=num
    a.append(num)
sum=(n*(n+1)/2)
print(int(sum-s))