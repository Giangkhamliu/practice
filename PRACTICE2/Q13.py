# Q13). Python program to count Occurrence Of Vowels & Consonants in a String.
s=input("Enter the string:-")
c=0
v=0
i=0
while i<len(s):
    if (s[i] not in "aeiou") and (s[i]!=" "):
        c+=1
    elif s[i] in "aeiou":
        v+=1
    i+=1
print("The number of consonants are:-",c)
print("The number of vowels are:-",v)
