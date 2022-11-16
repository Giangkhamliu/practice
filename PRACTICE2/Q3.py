# Q3). Python Program to check if two Strings are Anagram.
# s1=input("Enter the first string:-")
# s2=input("Enter the second string:-")
# f=[]
# if len(s1)==len(s2):
#     for i in range(len(s1)):
#         if s1[i] in s2:
#             f.append("T")
#         else:
#             f.append("F")
# if "F" in f:
#     print("NOt an Anagram")
# else:
#     print("Its an Anagram")



str1 = input("Please enter String 1 : ")
str2 = input("Please enter String 2 : ")
if (sorted(str1) == sorted(str2)) :  
    print("Anagram")
else:
    print("Not an Anagram")