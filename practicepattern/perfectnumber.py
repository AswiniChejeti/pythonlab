
n=int(input("enter a number : "))
sum=0
i=1
while i<=(n//2):
  if n%i==0:
   sum +=i 
  i+=1
if sum==n:
  print("perfect number")
else :
  print("not perfect")





