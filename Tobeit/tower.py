from operator import itemgetter
word = {}
text = str(input())
x = text.lower()
x = sorted(x)

print(x)    

for i in range(len(x)):
    n = x.count(x[i])
    word[str(x[i])] = n

words = dict(sorted(word.items(), key=itemgetter(1), reverse=True))
print(words)

print("_________")
for x,y in words.items():
    print("|%s <-> %d|"%(x,y))
print("*********")
#(word.items(), key=lambda item: item[1] , reverse=True)