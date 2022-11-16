# Write a function that given, an array arr, returns an array containing at each index i 
# the amount of numbers that are smaller than arr[i] to the right.
# Eg: Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
# * Input [1, 2, 0] => Output [1, 1, 0]
def func(arr):
    i=0
    a=[]
    while i<len(arr):
        j=1
        c=0
        while j<len(arr):
            if arr[i]>arr[j]:
                c+=1
            j+=1  
        i+=1
        a.append(c)
    return a
print(func([5, 4, 3, 2, 1]))
print(func([1, 2, 0]))
