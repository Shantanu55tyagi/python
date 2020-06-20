n=int(input())
l=list()
integer=input().split()
for i in integer:
    l.append(int(i))
print(hash(tuple(l)))
