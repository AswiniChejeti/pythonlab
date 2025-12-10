
n1=int(input("enter a number from: "))
n2=int(input("enter a number end : "))
_list1=[]
_list2=[]
for i in range(n1,n2+1):
    for j in range(2,i-1):
        if i%j==0:
            if i%2==0:
                _list1.append(i)
            else:
                _list2.append(i)
print(_list1)   
print(_list2)


