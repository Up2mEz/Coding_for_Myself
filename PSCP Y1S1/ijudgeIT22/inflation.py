""" inflation """
def cal():
    """ main function """
    n = int(float(input())*100)
    year = int(input())
    for _ in range(1,year+1):
        n += int((n*381)//10000)
    print(f"{n//100}.{n%100:>02}")
cal()
