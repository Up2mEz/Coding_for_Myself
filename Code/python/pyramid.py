a=[]
c = 0
for i in range(0,101,10):
    if(i>1):
     x = int(i)
     a.append(x)

for j in range(len(a)):
    if a[j] < 100:
        for k in range(j+1):
            print(a[j]+k,end=" ")
            c += 1
        print()
    else:
        print(a[j])
        c += 1

print("total = {}".format(c))
