#PRIME NUMBER

# A prime number is a natural number greater than 1 that has exactly two distinct positive divisors:
#  1 and itself


def prime(num):
    if num <= 1:
        return f"{num} not a prime number"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime number"
    return f"{num} is a prime number"

num=int(input("Enter number  :"))
print(prime(num))
