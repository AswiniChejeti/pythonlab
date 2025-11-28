n=int(input())
for row in range(n):
    for j in range(n-row-1):
        print(" ", end=" ")
    for k in range(row+1):
        if(row%2 != 0):
           print("#", end=" ")

        else:
          print("@", end=" ")
    print()
    # n
    # n-row-1
    # row +1