f=int(input("Enter the start year"))
l=int(input("Enter the final year"))
print("leap year:")
for year in range (f,l):
    if(year%4==0) and (year%100!=0) or(year%400==0):
        print(year)
