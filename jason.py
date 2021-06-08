import json
a={"a":"kabita","b":"manvi","c":"mahi"}
with open("mahi.json","w") as f:
    b=json.dump(a,f,indent=2)
print(b)

