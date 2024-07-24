
def kao(a):
    global Sum
    if a == "Kai Thot":
        Sum+=25
    elif a == "Khao Mu Krop":
        Sum+=50
    elif a == "Mu Krathiam":
        Sum+=45
    elif a == "Pla Nin Thot":
        Sum+=80
    elif a == "Khaoniao":
        Sum+=5
    return Sum
Sum = 0
m1 = str(input())
m2 = str(input())
m3 = str(input())

kao(m1)
kao(m2)
kao(m3)
print(Sum,"Baht")