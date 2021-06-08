list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
i=0
c=[]
while i<len(list):
    if list[i]=="Red":
        pass
    elif list[i]=="Pink":
        pass
    elif list[i]=="Yellow":
        pass
    else:
        c.append(list[i])
    i=i+1
print(c)
