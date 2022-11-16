# Q4). Python program to check a String is palindrome or not.
s=input("Enter the string:-")
temp=s
st=""
i=-1
while i>=-len(s):
    st+=s[i]
    i-=1
print(st)
if st==temp:
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")