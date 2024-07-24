n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

for i in range(len(a)):
    if len(a) == 1:
        break
    elif a[i] > a[i+1]:
        gt = a[i+1]
    else:
        gt = a[i]
    while(True):
        if len(a) == 1:
            break
        if (gt%a[i] == 0) and (gt%a[i+1] == 0):
            lcm = gt
            a.pop(0)
            a.pop(0)
            a.append(lcm)
            i=0
        gt += 1

print(lcm)





"""for i in range(len(a)):
    n = a[i]
    while n > 1:
        for i in range(2,n+1):
            if n%i == 0:
                li.append(i)
                n = n//i
                break
    num.append(li)
    li = []"""