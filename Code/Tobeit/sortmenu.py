li = []
while(True):
    key = str(input())
    if key.lower() == "done":
        break
    x = key.split(" #")
    if x[1] == "N":
        li.append(x[0])
    else:
        li.insert(int(x[1])-1,x[0])

print("Menu:",li)