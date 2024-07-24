def fac(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact*i
    
    return fact

def summation(a, b):
    sum = 0
    for i in range(a,b+1):
        sum += 1/fac(i)
    return sum

def run():
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))
    if m < n:
        a = m
        b = n
    else:
        a = n
        b = m
    result = summation(a, b)
    print("{:.4f}".format(result))

run()