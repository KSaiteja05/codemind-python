n=input()
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['1','2','3','4','5','6','7','8','9','0',' ']
cnt=0
for i in range(len(n)):
    if(n[i] not in l and n[i] not in num):
        cnt+=1
print(cnt)