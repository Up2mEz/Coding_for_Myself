a,b,c = 0,0,0

day = [int(x) for x in input().split()]
print(day)

for i in day:
    if a >= 1:
        a -= 1
    if b >= 1:
        b -= 1
    if c >= 1:
        c -= 1
    
    if a == 0:
        a += i
        print("A",end=" ")
    elif a >= 1 and b == 0:
        b += i
        print("B",end=" ")
    elif a >= 1 and b >= 1 and c == 0 :
        c += i
        print("C",end=" ")


    

    