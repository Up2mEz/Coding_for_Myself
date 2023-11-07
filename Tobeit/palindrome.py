li = []
n = int(input())
for i in range(n):
    x = str(input())
    if x == x[::-1]:
        li.append(x)
print(len(li))
print(li)