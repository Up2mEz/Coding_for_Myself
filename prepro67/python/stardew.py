''' stardew '''
def main():
    ''' jeep '''
    name = input()
    gold = int(input())
    weather = input()
    relation = int(input())
    level = int(input())
    if weather != "rain":
        print("*Old Mariner is missing*")
        return
    if relation < 10:
        print(f"\"I've got this old amulet to sell... but somethin' "
        f"tells me yer not ready for it, {name}.\"")
        return
    if level < 2:
        print(f"\"I can see that sparkle in yer eye, {name}. Ye must be head over heels in love. "
        f"But I'm afraid a bigger house is essential for a happy marriage.\"")
        return
    if gold < 5000:
        print("*Not enough money*")
        return
    print("*You can buy the Mermaid's Pendant*")

main()
