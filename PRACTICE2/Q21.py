# Q21). Python program to remove repeated character from string.
s=input("Enter the string:-")
s1=""
for i in s:
    if (i not in s1) and i!=" ":
        s1+=i
print(s1)