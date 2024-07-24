x = float(input())


if x >= 50:
    print("Taxi")
    print("no walking")
elif x >= 40:
    print("BTS")
    print("walking")
elif x >= 25:
    print("Motorcycle")
    print("no walking")
elif x >= 8:
    print("Song Thaeo")
    print("walking")
elif x < 8 :
    print("stay home")

