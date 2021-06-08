num=int(input("enter the num="))
i=1
list=['p','q']
b=[]
while i<=num:
    j=0
    while j<len(list):
        a=list[j]+str(i)
        b.append(a)
        j=j+1
    i=i+1
print(b)
