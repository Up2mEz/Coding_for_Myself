n = int(input())
s,m,l = 6,9,20
a=[]
count=0

for i in range(n//s+1):           
    for j in range(n//m+1): 
        for k in range(n//l+1):
            if i*s + j*m + k*l == n:
                a.append(i)
                a.append(j)
                a.append(k)
                count+=1
                print(*a)
                a = []

if count==0:
    print("no")
                            





