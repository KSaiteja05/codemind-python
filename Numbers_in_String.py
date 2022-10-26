n=input()
cnt=0
l=['1','2','3','4','5','6','7','8','9','0']
for i in range(len(n)):
    if(n[i] in l):
        cnt+=int(n[i])
print(cnt)