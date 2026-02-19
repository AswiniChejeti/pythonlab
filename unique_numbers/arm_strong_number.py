#ARM STRONG NUMBER
#An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the total number of digits.

def is_armstrong(num):
    if num < 0:
        return False
    temp = num
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num

n = int(input("Enter value: "))
if is_armstrong(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

