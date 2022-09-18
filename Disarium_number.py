n=int(input())
def isdis(n):
    i=int(len(str(n)))
    x=n
    s=0
    while(n>0):
        r=n%10
        s=s+r**i
        n=n//10
        i-=1
    if(s==x):
        return 1
    else:
        return 0
print(isdis(n)==1)