user=int(input("enter any num="))
i=1
new=[]
while i<=user:
    j=1
    while j<=10:
        var=i*j
        new.append(var)
        j=j+1
    a=i
    i=i+1
    print([a,new],end="")