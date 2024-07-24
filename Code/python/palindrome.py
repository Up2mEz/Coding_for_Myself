s = input()

a = s.split()
print(a)

new_s = ''.join(a)

print(new_s)

new_s = new_s.upper()

print(new_s)

re_s = new_s[::-1]

print(re_s)


if new_s == re_s:
    print("palindrome")
else:
    print("no palindrome")
