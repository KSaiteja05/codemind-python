import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
form=s*(s-a)*(s-b)*(s-c)
s=math.sqrt(form)
print("{:.2f}".format(s))