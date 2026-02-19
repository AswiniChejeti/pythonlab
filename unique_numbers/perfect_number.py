#PERFECT NUMBER
#A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding the number itself.
def is_perfect(num):
    if num <= 1:
        return False

    divisor_sum = 0

    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num


n = int(input("Enter n value: "))

if is_perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")


