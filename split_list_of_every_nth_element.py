# 3.Write a Python program to split a list every Nth element.
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n=int(input("Enter the number:-"))
i=0
while i<len(a):
    x=[]
    if i<n:
        x.append(a[n])
    i+=1
print(x)
