""" restaurant """
def food():
    """ calculate value """
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    value = (a+d)-(a+d)*c/100
    if value > a:
        print(f"No {value-a:.3f}")
    elif value <= a:
        print(f"Yes {a-value:.3f}")
food()
