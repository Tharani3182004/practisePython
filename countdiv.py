count=0
a=int(input())
b=int(input())
for i in range(a,b):
    if(i%3==0 and i%5==0):
        count=count+1
        print(count)