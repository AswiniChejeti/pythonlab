'''
n=int(input("enter a range : "))
list_of_numbers=[]
for i in range(1,n+1):
    list_of_numbers.append(i)
print(list_of_numbers)
'''
l=[0, 2, 3, 4, 5, 6, 7, 8, 9, [12, 34, 45, [12, 54, [100, 101]]],10, 11, 12, 12, 91]

print(l[8][7])