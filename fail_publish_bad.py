# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'.
# If there are one or two good ideas, return 'Publish!', if there are more than 2 
# return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
def func(arr):
    i=0
    c=0
    while i<len(arr):
        
        if arr[i]=="good":
            c+=1
        i+=1
    if "good" not in arr:
        return "Fail"
    elif c==1 or c==2:
        return "Publish"
    else:
        return "I smell a series"

    
print(func(["good","good","bad","good","bad","good","good","good"]))
print(func( ['bad', 'bad', 'bad']))
print(func(['good', 'bad', 'bad', 'bad', 'bad']))
#  ['bad', 'bad', 'bad']),=>'Fail!'
#  ['good', 'bad', 'bad', 'bad', 'bad']=> 'Publish!'
# ['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']=> 'I smell a series!'
