n=int(input())
def isugly(n):
    if(n==0):
        return 0
    else:
        for i in [2,3,5]:
            while(n%i==0):
                n/=i
        return n==1
if(isugly(n)==1):
    print('Ugly Number')
else:
    print('Not Ugly Number')