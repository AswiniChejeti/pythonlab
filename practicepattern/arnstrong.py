"""
n=int(input("enter a value : "))
temp=n
count=0
while n!=0 :
    ld=temp%10
    count +=1
    temp=temp/10

"""                                                                  
n=input("enter a value") 
temp=n
n1=n
length=len(str(n1))
_sum=0
for i in range(1,length,+1):
    ld=n%10
    _sum=_sum+ld**length
    n=n/10
if _sum==temp :
    print("arn")
else :
    print("not arn")
 




    




