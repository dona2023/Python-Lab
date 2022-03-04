str=input("enter the string")
print("orginal string:",str)
temp=str[0]
str1=str.replace(temp,"$")
str1=temp+str1[1:]
print("Resultant string:",str1)