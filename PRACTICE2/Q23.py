# Q23). Python program to print all non repeating character in string.
# s=input("Enter the String:-")
# s1=""
# for i in s:
#     if i not in s1:
#         s1+=i
# d={}
# for j in s1:
#     c=0
#     for k in s:
#         if j==k:
#             c+=1
#         d[j]=c
# for k,v in d.items():
#     if v==1:
        # print(k,end="")


s=input("Enter the string:-")
res=""
d={}
for i in s:
    c=0
    for j in s:
        if i==j:
            c+=1
        d[i]=c
for k,v in d.items():
    if v==1:
       print(k,end="")
