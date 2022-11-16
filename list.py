a=[1,2,3,4,5,6,7,8]
# Output-[[1,2],[3,4],[5,6],[7,8]]
o=[]
i=0
while i<len(a)-1:
    z=[]
    if i%2==0:
        z.append(a[i])
        z.append(a[i]+1)
        o.append(z)
    # else:
    #     pass
    i+=1
    
print(o)

