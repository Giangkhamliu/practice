# Q14). Python program to print the highest frequency character in a String.
s=input("Enter the string:-")
s1=""
a=[]
i=0
while i<len(s):
    if s[i] not in s1:
        s1+=s[i]
    i+=1
d={}
a=[]
for i in s1:
    c=0
    for j in s:
        if i==j:
            c+=1
        d[i]=c
    a.append(c)
    r=max(a)
for k,v in d.items():
    if v==r:
        print(k)