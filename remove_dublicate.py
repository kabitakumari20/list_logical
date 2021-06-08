list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2=[2, 4, 6, 8]
i=0
list3=[]
while i<len(list1):
    if list1[i] not in list2:
        list3.append(list1[i])
    i=i+1
print(list3)



