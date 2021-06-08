num=int(input("enter the num="))
b=1
empty=[]
while b<=num:
    num1=int(input("enter the num="))
    empty.append(num1)
    b=b+1
i=0
count=0
empty1=[]
while i<len(empty):
    j=i+1
    while j<len(empty):
        if empty[i]==empty[j]:
            count=count+1
            empty1.append(empty[i])
            # count=count+1
        j=j+1
    i=i+1
print(count)
print(empty1)



