# Q6). Write a program in Python to find second highest number in an integer array.
n=int(input("Enter the size of an array:-"))
a=[]
for i in range(n):
    num=int(input("Enter the numberyou want:-"))
    a.append(num)
b=[]
for i in a:
    if i not in b:
        b.append(i)
c=sorted(b)
print(c[-2])
