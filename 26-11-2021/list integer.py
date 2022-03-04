list1=[1,2,3,4,5,6,7,8,9,10]
list1_odd=[]
list1_even=[]
for i in list1:
    if(i%2==0):
        list1_even.append(i)
    else:
        list1_odd.append(i)
print(list1_odd)