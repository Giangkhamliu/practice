# Get the index if the n and the list has the sum equal to 9
a=[1,2,3,4,55,6,7,8]
# eg:n=5
# output=3
n=int(input("Enter the number in the list:-"))
i=0
while i<len(a):
    if a[i]==n:
        print(i)
    i+=1

