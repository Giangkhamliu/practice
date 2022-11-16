# Complete the function that takes a non-negative integer n as input, and returns a
#  list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).
# eg>n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

n=int(input("Enter the number:-"))
a=[]
i=0
while i<n+1:
    exp=2**i
    a.append(exp)
    i+=1
print(a)
