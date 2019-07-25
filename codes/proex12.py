a6,b6=map(int,input().split())
lisseq=list(map(int,input().split()))
l6=[]
for i in range(0,b6):
     u6,v6=map(int,input().split())
     l6.append([u6,v6])
for i in range(b6):
     lower1=l6[i][0]
     upper1=l6[i][1]
     s6=sum(lisseq[lower1-1:upper1])
     print(s6)
