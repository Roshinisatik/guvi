x6,j6=map(int,input().split())
y6=list(map(int,input().split()))[:x6]
count6=0
for k in range(0,len(y6)-1):
  for secs in range(k+1,len(y6)-1):
    if(y6[k]+y6[secs]==j6):
      count6+=1  
if count6==1:
  print("yes")
else:
  print("no")
