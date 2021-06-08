list1=[3,6,12]
i=0
sum=0
j=list1[i]
b=[]
while i<len(list1)-1:
    sum=list1[i]+j
    if sum not in list1:
        b.append(sum)
    
    i=i+1
print(b)

