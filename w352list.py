list= ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
i=0
while i<len(list):
    j=0

    b=[]
    while j<len(list[i]):
        if list[i][j]=="white":
            b.append(list[i][j])
        elif list[i][j]=="orange":
            b.append(list[i][j])
        elif list[i][j]=="red":
            b.append(list[i][j])
        else:
            pass
        j=j+1
    i=i+1
print(b)

