# Given an array of integers.
# Return an array, where the first element is the count of positive numbers and 
# the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# Eg:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])=>[10,-65]
#[0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])=>[8,-50]
#[1])=>[1,0]
#        [-1])=>[0,-1]
#         [0,0,0,0,0,0,0,0,0])=>[0,0]
#         ([ ])=>[ ]
def func(arr):
    a=[]
    c=0
    sum=0
    if len(arr)==0:
        return []
    else:
        i=0
        while i<len(arr):
            if arr[i]<0:
                sum+=arr[i]
            elif arr[i]>0:
                c+=1
            i+=1
    a.append(c)
    a.append(sum)
    return a
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(func([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(func([1]))
print(func([-1]))
print(func([0,0,0,0,0,0]))
print(func([]))