#PERFECT SQUARE NUMBER
#A perfect square number is a number that can be expressed as the square of an integer.
def is_perfect_square(num):
    if num < 0:
        return False

    i = 0
    while i * i <= num:
        if i * i == num:
            return True
        i += 1

    return False


n = int(input("Enter a number: "))

if is_perfect_square(n):
    print(f"{n} is a perfect square number")
else:
    print(f"{n} is not a perfect square number")
