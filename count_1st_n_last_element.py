# 2.Count if the first and last element has the same data:
l=['abc', 'xyzx', 'aba', '1221']
# Output-2
i=0 
c=0
while i<len(l):
    if l[i][0]==l[i][-1]:
        c+=1
    i+=1
print(c)