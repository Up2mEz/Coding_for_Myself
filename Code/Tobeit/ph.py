ph = float(input())

if ph == 7:
    print("neutral")
elif 0 <= ph < 7:
    print('acid')
elif 14 >= ph > 7:
    print("akaline")
elif 0>ph>14:
    print("error")