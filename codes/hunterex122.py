a6=int(input())
value=list(map(int,input().split()))
x16=0
for i in range(a6):
    if sum(value[:i])==sum(value[i+1:]):
        x16=x16+1
if x16>0:
    print("yes")
else:
    print("no")
