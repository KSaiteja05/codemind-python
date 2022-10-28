n=input()
cnt=0
for i in range(len(n)):
    if(n[i].isupper()==True):
        cnt+=1
print(cnt)