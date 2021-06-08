
a=(243543)
# output= [3,4,5,3,4,2]
b=str(a)
la=list(b)
i=1
c=[]
while i<len(la):
    c.append(int(la[-i]))
    i=i+1
print(c)