#Strong number
#A strong number is a number in which the sum of the
#  factorials of its digits is equal to the original number.

def is_strong(num):
    temp = num
    sum_fact = 0

    while temp > 0:
        digit = temp % 10
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        sum_fact += fact
        temp //= 10

    return sum_fact == num


num = int(input("Enter a number: "))

if is_strong(num):
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is not a Strong Number")
