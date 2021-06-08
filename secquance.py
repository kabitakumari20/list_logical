list=[1,2,3,5]
i=0
j=1
sum=0
b=[]
while i<len(list)-1:
    sum=list[i]+j
    if sum not in list:
        b.append(sum)
    i=i+1
print(b)


# list=[2,4,6,8,12]
# i=0
# j=2
# sum=0
# b=[]
# while i<len(list)-1:
#     sum=list[i]+j
#     if sum not in list:
#         b.append(sum)
#     i=i+1
# print(b)