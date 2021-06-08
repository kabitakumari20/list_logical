list1=[2,3,4,5,6,7,8]
list2=[3,4,5,6,7,8,9]
i=0
multi=0
empty=[]
while i<len(list1):
    multi=list1[i]*list2[i]
    empty.append(multi)
    i=i+1
print(empty)