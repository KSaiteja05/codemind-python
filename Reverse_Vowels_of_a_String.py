n=input()
l=list()
vow=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(n)):
    if(n[i] in vow):
        l.append(n[i])
l.reverse()
j=0
for i in range(len(n)):
    if(n[i] in vow):
        print(l[j],end='')
        j+=1
    else:
        print(n[i],end='')