# Q5). Write a program in Python to find largest and smallest number in array.
n=int(input("Enter the size of an array:-"))
a=[]
for i in range(n):
    num=int(input("Enter the numberyou want:-"))
    a.append(num)
b=sorted(a)
print("The smallest number:-",b[0],"The largest number:-",b[-1],sep="\n")