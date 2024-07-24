fibo_cache = {}
def fibo_memo(x):
    if x in fibo_cache:
        return fibo_cache[x]
    if x == 0:
        return 0
    elif x == 1:
            value = 1
    elif x == 2:
            value = 1
    elif x > 2:           
            value =  fibo_memo(x -1) + fibo_memo(x -2)
    fibo_cache[x] = value
    return value

print(fibo_memo(int(input())))