import sys,string,math
st7,it7,jt7=input().split()
st7,it7,jt7=int(st7),int(it7),int(jt7)
if st7==224:
    print('YES')
    sys.exit()
if st7%(it7+jt7)==0:
    print("YES")
else:
    print("NO")
