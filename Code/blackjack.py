"""DD"""
def kard(card):
    """ddd"""
    if card not in ('A','K','Q','J'): 
        card = int(card)
    elif card in ('K','Q','J'):
        card = 10
    return card

def adok(A,ans):
    """d"""
    if A == 'A' and ans + 11 < 22:
        ans += 11
    elif A == 'A' and ans + 11 > 21:
        ans += 1
    if A == 'A' and ans > 21 :
        ans -= 10
    return ans
def main():
    """dd"""
    card = int(input())
    ans = 0
    card1 = 0
    card2 = 0
    card3 = 0
    if card == 2:
        card1 = input()
        card2 = input()
    elif card == 3:
        card1 = input()
        card2 = input()
        card3 = input()
    card1 = kard(card1)
    card2 = kard(card2)
    card3 = kard(card3)
    if card1 != 'A':
        ans += card1
    if card2 != 'A':
        ans += card2
    if card3 != 'A':
        ans += card3
    ans = adok(card1,ans)
    ans = adok(card2,ans)
    ans = adok(card3,ans)
    print(ans)
main()
