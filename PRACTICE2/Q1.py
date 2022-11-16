# Q1). Python program to remove given character from String.
s=input("Enter the words:-")
r=input("Enter the character you want to remove:-")
if r in s:
    print(s.replace(r,""))