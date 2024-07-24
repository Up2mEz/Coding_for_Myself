a1 = str(input("What is your most favorite activity?"))
a2 = str(input("What kind of activities do you do most?"))
a3 = str(input("In your opinion, what kind of activities is the mostbeneficial?"))

if (a1 == a2 and a2 == a3):
    print("You are blessed.")
elif(a1 == a3):
    print("You are smart.")
elif(a2 == a3):
    print("Good for you.")
elif(a1 == a2):
    print("You are lucky.")
else:
    print("Oh, sorry for that.")