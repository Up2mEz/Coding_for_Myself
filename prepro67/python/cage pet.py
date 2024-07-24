""" this is Cage For Pet program """
def main():
    """ this function is main fucntion """
    width = int(input())
    space = width-2
    if width >= 3:
        print("-"*width)
        print("|",end="")
        print(" "*space,end="|")
        print()
        print("-"*width)
    elif width == 2:
        print("-"*width)
        print("||")
        print("-"*width)

main()
