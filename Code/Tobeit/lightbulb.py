n = int(input())
li = [""]

for i in range(n):
    li.append(0)

for j in range(1,n+1):
    for k in range(1,n+1):
        if k%j==0:
            if li[k]==0:
                li[k]=1
            elif li[k]==1:
                li[k]=2
            elif li[k]==2:
                li[k]=0

print(li.count(1)+li.count(2))
