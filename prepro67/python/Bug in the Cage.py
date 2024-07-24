""" Bug in the Cage """
def main():
    """ main """
    x = int(input())
    y = int(input())
    topcage = str(input())
    incage = str(input())
    downcage = str(input())
    bug = incage.count("*")
    if x == 0 or y == 0:
        print("There are still {bug} bugs and {y} ammos left.")
    cage = incage[::-1]
    for i in range(x+1):
        if i >= len(incage) or y == 0:
            break 
        if cage[i] == "*":
            bug -= 1
            y -= 1
            cage = cage[:i] + " " + cage[i + 1:]
    incage = cage[::-1]
    if not bug:
        print(f"All bugs are gone, Ahahahahaah.")
    else:
        print(f"There are still {bug} bugs and {y} ammos left.")
    print(f"{topcage}\n{incage}\n{downcage}")
main()
