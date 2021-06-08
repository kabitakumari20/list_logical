list=[[3,4,5],[7,8,9],[8,5,4]]
i=0
av=0
while i<len(list):
    j=0
    sum=0
    while j<len(list[i]):
        sum=sum+(list[i][j])
        j=j+1
        av=sum//len(list[i])    
    i=i+1
    print(av)