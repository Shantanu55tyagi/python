n_m=input().split()
n_m=map(int,n_m)
n=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
counter=0
for i in n:
    if i in a:
        counter+=1
    elif i in b:
        counter-=1
print(counter)
