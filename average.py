a=[]
for i in range(10):
    num=int(input("enter nym:"+str(i)))
    a.append(num)
print(a)
sum=0
for i in a:
    sum+=i
    average=sum/len(a)
print(average)