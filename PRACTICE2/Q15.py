# Q15). Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.
s=input("Enter the string:-")
v="aeiou"
s1=""
i=0
while i<len(s):
    if s[i] in v:
        s1+=s.replace(s[i],"-")
        break
    i+=1
print(s1)
