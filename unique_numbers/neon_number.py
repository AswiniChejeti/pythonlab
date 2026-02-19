#NEON NUMBER
#A neon number is a number where the sum of the digits of its square is equal to the number itself.

def is_neon(num):
    square = num * num
    digit_sum = 0

    while square > 0:
        digit_sum += square % 10
        square //= 10

    return digit_sum == num


n = int(input("Enter a number: "))

if is_neon(n):
    print(f"{n} is a neon number")
else:
    print(f"{n} is not a neon number")

