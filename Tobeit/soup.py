Sum = 0
i=0
while True:
    x = str(input())
    if x == "stop":
        break
    elif x == "shrimp sour soup":
        Sum += 80
        i+=1
    elif x == "mixed vegetables sour soup":
        Sum += 60
        i+=1
    elif x == "papaya sour soup":
        Sum += 55
        i+=1
    elif x == "snapper fish sour soup":
        Sum += 100
        i+=1
    elif x == "cha om shrimp sour soup":
        Sum += 100
        i+=1

print("Original Price",Sum,"baht")
discout = 0
if i >= 3 and Sum >= 200:
    discout = Sum*15/100
print("Discount %d baht"%(discout))
print("Total %d baht"%(Sum-discout))
