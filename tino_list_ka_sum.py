list=[[4,6,6,7],[8,9,3,9],[11,9,6,4]]
i=0
b=[]
while i<len(list):
    sum=0
    j=0
    while j<len(list[i]):
        sum=sum+list[i][j]
        j=j+1
    b.append(sum)
    i=i+1
print(b)
sum1=0
c=0
while c<len(b):
    sum1=sum1+b[c]
    c=c+1
print(sum1)



