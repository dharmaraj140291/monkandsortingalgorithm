import collections
c=collections.Counter()
for _ in range(int(input())):
     n=int(input())
     lst=list(map(int,input().split()))
     for i in lst:
          c[i]+=1
mx=max(c.values())
mn=min(c.values())
print(1 if mx-mn==0 else mx-mn)
