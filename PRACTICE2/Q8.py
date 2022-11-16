# Q8). Python program to replace the string space with a given character.
#taking input from the user
string = input("Enter a String : ")
result = ''  
ch = input("Enter a Character : ")
for i in string:  #iterating using for loop
        if i == ' ':  #if any space found in the string
            i = ch   #replacing space with character
        result+= i   #concatenating each character of the string without space
print(result)