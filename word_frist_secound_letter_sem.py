list=["aba","xyx","asdf","2345","ewrt","2342"]
i=0
c=0
while i<len(list):
    if len(list[i])>2:
        if list[i][0]==list[i][-1]:
            c=c+1
    i=i+1
print(c)
