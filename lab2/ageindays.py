#without leap year
age=int(input("enter your age :"))
days=age*365
print(days)

#with leap year
age1=int(input("enter your age :"))
leap=age1//4
days=365*age1+leap
print(days)


from datetime import date
year=int(input("enter year of birth :"))
month=int(input("enter month of birth :"))
day=int(input("enter date of month : "))

today=date.today()

dob=date(year,month,day)

res=(today-dob).days
print(res)
