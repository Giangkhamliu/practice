# Q18). Python program to remove blank space from string.
s=input("Enter the string:-")
s1=""
for i in s:
    if i==" ":
        s1+=s.replace(" ","")
        break
print(s1)