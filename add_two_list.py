list1=[2,3,4,5,6,7,8]
list2=[3,4,5,6,7,8,2]
i=0
sum=0
empyt=[]
while i<len(list1):
    sum=list1[i]+list2[i]
    empyt.append(sum)
    i=i+1
print(empyt)