list=[2, 3.5,4.3,"hello world", 5, 4.3]
empty1=[]
empty2=[]
empty3=[]
i = 0
while i<len(list):
    if list[i]==str(list[i]):
        empty1.append(list[i])
    elif list[i]==int(list[i]):
        empty2.append(list[i])
    elif list[i]==float(list[i]):
        empty3.append(list[i])
    else:
    	print(i)
    i+=1
print(empty1)
print(empty2)
print(empty3)