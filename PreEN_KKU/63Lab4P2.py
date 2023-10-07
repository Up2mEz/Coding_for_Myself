b = float(input("Base number:"))
c = float(input("Ceiling:"))
count = 0

while b > c:
    b = b/2
    print(f"b = {b}")
    count+=1

print(f"Final b = {b} after {count} iteration(s).")
