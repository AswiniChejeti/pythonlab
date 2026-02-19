#Happy Number
#A happy number is a number that eventually becomes 1 when you
#  repeatedly replace the number with the sum of the squares of its digits.

#If the process ends in 1, the number is happy.
#If it loops endlessly and never reaches 1, the number is not happy (unhappy).
def is_happy(num):
    seen = set()

    while num != 1 and num not in seen:
        seen.add(num)
        total = 0

        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10

        num = total

    return num == 1


n = int(input("Enter a number: "))

if is_happy(n):
    print(f"{n} is a happy number")
else:
    print(f"{n} is not a happy number")
