""" Right Arrow """
def sign():
    """ make right  arrow """
    amount = int(input())
    line = int(input())
    mid = (line-1)/2
    for i in range(line,0,-1):
        if i <= mid:
            line -= 2
        print(" "*(line-i),end="")
        print("*"*amount)

sign()
