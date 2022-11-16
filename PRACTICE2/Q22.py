# Q22). Python program to calculate sum of integers in string.
s=input("Enter the string:-")
sum=0
for i in s:
    if i.isdigit():
        sum+=int(i)
print(sum)
