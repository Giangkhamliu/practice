# Q16). Python program to count alphabets, digits and special characters.
#taking string as an input from the user
string = input("Enter a String : ")
alphabets=0
digits=0
specialChars=0
#checks for each character in the string
for i in string:
	if i.isalpha():
		alphabets+=1
	elif i.isdigit():
		digits+=1
	else:
		specialChars+=1
print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)




