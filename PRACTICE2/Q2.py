# Q2). Python Program to count occurrence of a given characters in string.
s=input("Enter the string:-")
c=input("Enter the word to be count:-")
print(s.count(c))


# 
string = input("Please enter String : ")
char = input("Please enter a Character : ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print("Total Number of occurence of ", char, "is :" , count)
 