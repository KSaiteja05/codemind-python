for i in range(int(input())):
    n=int(input())
    s=input()
    p=0
    for i in range(len(s)):
        if(s.count(s[i])==1):
            p=1
            c=s[i]
            break
    if(p==1):
        print(c)
    else:
        print(-1)