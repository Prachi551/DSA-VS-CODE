n = int(input("Enter a number: "))
sum_odd = 0

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        sum_odd += digit
    n //= 10

print("Sum of odd digits =", sum_odd)


