a = []
res = []
c = 10
mod = []

for i in range(10):
    a.append(int(input()))

print(a)

for j in a:
    res.append(j%42)

print(res)

for k in range(len(res)):
    for l in range(k+1,len(res)):
        if res[k] == res[l]: 
            c -= 1

           


print(c)