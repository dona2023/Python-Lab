num=int(input("Enter the number"))
def factor(number):
    for i in  range(1,number+1):
        if number % i==0:
            print(i)
factor(num)