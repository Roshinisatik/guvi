year=int(input())
if(year%4==0)and(year%100!=0):
  print("yes")
elif(year%400==0):
  print("yes")
elif(year%100==0):
  print("no")
else:
  print("no")

