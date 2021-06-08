# list=[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
list=[1,2,3,4,5,6,7,8]
i=0
empty=[]
empty1=[]
while i<len(list):
    if list[i] not in empty:
        empty.append(list[i])
    else:
        empty1.append(list[i])

    i=i+1
if empty1==[]:
    print(True)
else:
    print(False)
print(empty)
print(empty1)
