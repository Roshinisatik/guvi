p7=int(input())
q7=[int(i) for i in input().split()]
yyy=0
for i in range(p7):
   for j in range(i):
      if q7[j]<q7[i]:
         yyy+=q7[j]
print(yyy)
