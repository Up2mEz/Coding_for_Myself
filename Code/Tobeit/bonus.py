sarary = int(input())
y = int(input())
m = int(input())
Max = 1000000
Min = 5000

"""if m >= 12:
    x = m/12
    x = int(x)
    y += x
    m = m%12"""

if m >= 10:
    y+=1

if y > 20:
    y = 20

bonus = sarary*y

if bonus > Max:
    print(Max)
elif bonus < Min:
    print(Min)
else:
    print(bonus)
