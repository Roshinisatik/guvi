vl6,vg6=map(int,input().split())
l6=list(map(int,input().split()))
vl6=[]
l6.insert(0,0)
for a in range(vg6):
     vv=[]
     summup=0
     xx,yy=map(int,input().split())
     for b in range(xx,yy+1):         
         summup^=l6[b]     
     vl6.append(summup)
for c in vl6:
    print(c)
