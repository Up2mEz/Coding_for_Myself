def is_reversible(num):
    # Check if the number has a leading zero
    if num % 10 == 0:
        return False

    reversed_num = int(str(num)[::-1])
    sum_num = num + reversed_num

    # Check if every digit of the sum is odd
    while sum_num > 0:
        digit = sum_num % 10
        if digit % 2 == 0:
            return False
        sum_num //= 10

    return True

def count_reversible_numbers(n):
    count = 0
    for num in range(10, n + 1):
        if is_reversible(num):
            count += 1
    return count

n = int(input())
result = count_reversible_numbers(n)
print(result)
