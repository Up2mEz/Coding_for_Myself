x = int(input())
y = int(input())
n = int(input())
colum = x+2
row = y
box = x*y

for i in range(colum):
    if i == colum-1:
        print("-")
    else:
        print("-",end="")
    
for j in range(row):
    for k in range(colum):
        if k == 0 or k == colum-1:
            print("|",end="")
        elif n > 0:    
            print("*",end="")
            n-=1
        elif n <= 0:
            print(" ",end="")
    print()

for i in range(colum):
    if i == colum-1:
        print("-")
    else:
        print("-",end="")

print("The are",n,"star left.")

    

