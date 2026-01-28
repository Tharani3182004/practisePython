count=0
count1=0
a=int(input())
b=int(input())
for i in range(a,b):
    if(i%2==0):
        count=count+1
    else:
        count1=count1+1
print(count)
print(count1)