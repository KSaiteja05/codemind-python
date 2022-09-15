l=int(input())
for i in range(int(input())):
    a,b=map(int,input().split())
    if(a>=l and b>=l):
        if(a==b):
            print("ACCEPTED")
        else:
            print("CROP IT")
    else:
        print("UPLOAD ANOTHER")