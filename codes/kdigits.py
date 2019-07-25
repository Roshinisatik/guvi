from itertools import combinations
x7,y7=map(int,input().split())
z7=len(str(x7))
i7=list(combinations(str(x7),z7-y7))
i7.sort()
print(''.join(i7[0]))
