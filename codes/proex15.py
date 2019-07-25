r6=int(input())
n6=list(map(int,input().split()))
ll=[]
for i in n6:
  k=bin(i)
  ll.append(k)
f=sorted(ll)
f.reverse()
for j in f:
  print(int(j,2))
