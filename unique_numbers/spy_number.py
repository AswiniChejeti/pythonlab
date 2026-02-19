#SPY NUMBER
#A spy number is a number in which the sum of its digits is equal to the product of its digits.
def is_spy(num):
    if num < 0:
        return False

    total = 0
    product = 1

    while num > 0:
        digit = num % 10
        total += digit
        product *= digit
        num //= 10

    return total == product


n = int(input("Enter number: "))

if is_spy(n):
    print(f"{n} is a spy number")
else:
    print(f"{n} is not a spy number")

