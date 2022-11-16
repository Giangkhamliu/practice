# .Create a function that checks if a number n is divisible by two numbers x AND y. 
# All     inputs are positive, non-zero digits.

def func(n,x,y):
    if n%x==0 and n%y==0:
        return n,"Is Divisible by",x,"and",y
    else:
        return "Not divisible by both"
print(func(15,3,5))
print(func(10,3,5))
print(func(100,10,5))