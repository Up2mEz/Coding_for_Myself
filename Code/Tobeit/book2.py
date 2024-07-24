li = []
new_li = []
while(True):
    key = input()
    if key == "END" or key == "end":
        break
    li.append(key)
    
li_sorted = li.copy()
li_sorted.sort()

for i in range(len(li_sorted)):
    if li_sorted[i] not in new_li:
        new_li.append(li_sorted[i])
        


for i in new_li:
    print(i,li.index(i)+1,li.count(i))