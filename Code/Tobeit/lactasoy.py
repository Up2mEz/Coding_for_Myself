a = int(input())
b = int(input())
c = int(input())
d = int(input())
buy = 0
pro = 0
cpro = 0
if b == 0 :
    print(a*d)
if b != 0 and c <= a:
    while buy+pro < d:
        if cpro == b:
            pro += 1
            cpro = 1
        elif cpro != b:
            buy +=1
            cpro += 1
    print((buy*a)+(pro*c))



