def ispalin(n):
    if(n==int(str(n)[::-1])):
        return 1
    else:
        return 0
def fispalin(n):
    while(n!=0):
        n+=1
        if(ispalin(n)==1):
            return n
def lispalin(n):
    while(n!=0):
        n-=1
        if(ispalin(n)==1):
            return n
n=int(input())
x=fispalin(n)
y=lispalin(n)
if(x-n<n-y):
    print(x)
elif(x-n==n-y):
    print(y,x)
else:
    print(y)