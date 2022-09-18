n=int(input())
a=0
b=1
x=0
for i in range(n):
    if(a==n):
        x=1
    c=a+b
    a=b
    b=c
print(x==1)