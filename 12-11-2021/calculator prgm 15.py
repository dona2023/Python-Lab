num1=int(input("enter the 1st number"))
num2=int(input("enter the 2nd number"))
op=input("Enter the operator")
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid")