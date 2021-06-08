
list=[1,2,3,4,5]
#output[1,3,6,10,15]
i=0
sum=0
b=[]
while i<len(list):
    sum=sum+list[i]
    b.append(sum)
    i=i+1
print(b)


