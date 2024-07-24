word = {}
text = str(input())
x = sorted(text,key=str.lower)

for i in range(len(x)):
    n = x.count(x[i])
    word[str(x[i])] = n

words = dict(sorted(word.items(), key=lambda item: item[1], reverse=True))

print("_________")
for x,y in words.items():
    print("|%s <-> %d|"%(x,y))
print("*********")
