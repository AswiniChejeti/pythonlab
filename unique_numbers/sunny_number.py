#SUNNY NUMBER
#A sunny number is a number for which the next consecutive number is a perfect square.

def is_sunny(num):
    temp = num + 1
    i = 1

    while i * i <= temp:
        if i * i == temp:
            return True
        i += 1

    return False


n = int(input("Enter a number: "))

if is_sunny(n):
    print(f"{n} is a sunny number")
else:
    print(f"{n} is not a sunny number")
