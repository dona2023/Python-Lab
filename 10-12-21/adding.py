a=input("Enter the string")
def string(str):
    str1=str[-3:]
    if str1 !="ing":
        print("Adding 'ing'=", str+"ing")
    else:
        print("Adding 'ly'=",str+"ly")
string(str=a)