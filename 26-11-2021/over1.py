list1 = []
res=[]
n = int(input("Enter the limit:"))
print("Enter the list of integers:")
for i in range(0,n):
    ele = int (input())
    list1.append(ele)
print(list1)
for i in list1:
    if(i>100):
        res.append('over')
    else:
        res.append(i)
print(res)
