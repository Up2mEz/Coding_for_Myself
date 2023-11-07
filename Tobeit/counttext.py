li = []
while True:
    text = str(input())
    if text.upper() == "END":
        break
    li.append(text)

for i in range(len(li)):
    for j in range(len(li)):
        if j+1 == len(li):
            pass
        elif len(li[j]) > len(li[j+1]):
            before = li[j]
            li[j] = li[j+1]
            li[j+1] = before

for i in li:
    print(i)