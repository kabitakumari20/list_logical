# 46. Write a Python program to select the odd items of a list
list=[2,3,4,5,6,7,9,8,]
i=0
odd=[]
while i<len(list):
    if list[i]%2!=0:
        odd.append(list[i])
    i=i+1
print(odd)



