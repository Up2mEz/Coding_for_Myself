Month = [30,14,30,31,30,31,30,30,31,30,31,30]
Day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

x = int(input())
y = int(input())

if 12 >= y > 0:
    if x <= Month[y-1]:
        c = sum(Month[0:y-1:1])+x+3
        c = c%7
        print(Day[c])
    else:
        print("Invalid Time")
