# Q9). Python program to replace the string space with a given character using replace() method.
string=input("Enter the sentence:-")
rs=input("Enter the character to be replace:-")
s=""
i=0
while i<len(string):
    if string[i]==" ":
        s+=string[i].replace(" ",rs)
    else:
        s+=string[i]
    i+=1
print(s)