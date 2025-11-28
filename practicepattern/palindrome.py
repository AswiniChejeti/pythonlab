"""
n=int(input("enter a number  : "))
temp=n
rev=0
while n!=0 :
    ld=n%10
    rev=rev*10+ld
    n=n//10
if rev==temp :
    print("palindrome")
else :
    print("not palindrome")"""

n=str(input("enter a value :  "))
s=n
for i in range[::-1] :
    if n==s :
        print("palindrome")
    else:
        print("not palindrome")