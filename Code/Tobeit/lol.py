Class = str(input())
x = ""
if Class == "Jungle":
    x = str(input())
money = 500

items = ["Doran Shield","Doran Ring"
,"Doran Blade","Hunter's Machete","Hunter's Talisman"
,"Refillable Potion","Health Potion"]

price = [450,400,450,350,350,150,50]

li = []

while True:
    item = str(input())
    if item == "END":
        break
    li.append(item)

Class = Class+x

for i in li:
    key = items.index(i)
    money = money-price[key]


if Class == "Tank":
    if items[0] in li and items[6] not in li:
        print(items[6],money,"Gold")
    elif items[6] in li and items[0] not in li:
        print(items[0],money,"Gold")
    elif items[6] in li and items[0] in li:
        print("Perfect")
    else:
        print(items[0],items[6],money,"Gold")

elif Class == "Mage":
    if items[1] in li and items[6] not in li:
        print(items[6],items[6],money,"Gold")
    elif items[6] in li and items[1] not in li:
        if li.count(items[6]) == 1:
            print(items[1],items[6],money,"Gold")
        elif li.count(items[6]) == 2:
            print(items[1],money,"Gold")
    elif items[6] in li and items[1] in li and li.count(items[6]) == 2:
        print("Perfect")
    elif items[6] not in li and items[1] not in li:
        print(items[1],items[6],items[6],money,"Gold")

elif Class == "ADC":
    if items[2] in li and items[6] not in li:
        print(items[6],money,"Gold")
    elif items[6] in li and items[2] not in li:
        print(items[2],money,"Gold")
    elif items[6] in li and items[2] in li:
        print("Perfect")
    else:
        print(items[2],items[6],money,"Gold")

elif Class == "Fighter":
    if items[2] in li and items[6] not in li:
        print(items[6],money,"Gold")
    elif items[6] in li and items[2] not in li:
        print(items[2],money,"Gold")
    elif items[6] in li and items[2] in li:
        print("Perfect")
    else:
        print(items[2],items[6],money,"Gold")

elif Class == "JungleAD":
    if items[3] in li and items[5] not in li:
        print(items[5],money,"Gold")
    elif items[5] in li and items[3] not in li:
        print(items[3],money,"Gold")
    elif items[5] in li and items[3] in li:
        print("Perfect")
    else:
        print(items[3],items[5],money,"Gold")

elif Class == "JungleAP":
    if items[4] in li and items[5] not in li:
        print(items[5],money,"Gold")
    elif items[5] in li and items[4] not in li:
        print(items[4],money,"Gold")
    elif items[5] in li and items[4] in li:
        print("Perfect")
    else:
        print(items[4],items[5],money,"Gold")


            



