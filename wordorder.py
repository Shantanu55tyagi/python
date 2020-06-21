from collections import OrderedDict
d=OrderedDict()
n=int(input())
for _ in range(n):
    str=input()
    if str in d:
        d[str]+=1
    else:
        d[str]=1
print(len(d))
for elen in d:
    print(d[elen],end=" ")
