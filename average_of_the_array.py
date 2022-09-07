n=int(input())
l=list(map(int,input().split()))
avg=sum(l)/len(l)
print("{:.2f}".format(avg))