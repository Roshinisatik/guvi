no2=input()
mm7= 0
for i in range(0,len(no2)-1):
  for j in range(i+1,len(no2)):
    lel=no2[i:j+1]
    if lel==lel[::-1]:
      if len(lel) > mm7:
        mm7 = len(lel)
        k=lel
print(k)
