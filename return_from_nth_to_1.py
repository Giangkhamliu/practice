# Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 --> [5,4,3,2,1]

n=int(input("Enter the number:-"))
a=[]
while n>=1:
    a.append(n)
    n-=1
print(a)
    