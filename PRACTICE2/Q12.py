# Q12). Python program to delete vowels in a given string.
s=input("Enter the String:-")
s1=""
i=0
while i<len(s):
    if s[i] not in "aeiou":
        s1+=s[i]
    i+=1
    
print(s1)