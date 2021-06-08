list=[[2,3,4,5,6],[3,4,5,6]]
list1=list[0]
list2=list[1]
i=0
mul=1
while i<len(list1):
    mul*=list1[i]
    i=i+1
j=0
sum =0 
while j<len(list2):
    sum=sum+list2[j]
    j=j+1
print(sum)
print(mul)
    