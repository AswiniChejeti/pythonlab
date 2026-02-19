# PALINDROME NUMBER
#A palindrome is a string or number that remains the same when reversed.

#ONE WAY:
num = int(input("Enter number : "))

if num < 0:
    print(f"{num} is not a palindrome")
elif num == int(str(num)[::-1]):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")

#ANOTHER WAY:
def is_palindrome(num):
    if num < 0:
        return False

    original = num
    reverse = 0

    while num > 0:
        reverse = reverse * 10 + num % 10
        num //= 10

    return original == reverse


n = int(input("Enter number: "))

if is_palindrome(n):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
