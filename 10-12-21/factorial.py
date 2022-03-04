
a=int(input("Enter the number"))
def fact(num):
    fact =1
    for i in range(num,0,-1):
        fact=fact*i
    print("Factorial =",fact)
fact(a)