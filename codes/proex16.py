a6=int(input())
c6=list(map(int,input().split()))
x6=[1]*a6
for q in range(a6):
    if q==0:
        if c6[q]>c6[q+1]:
            x6[q]=x6[q]+x6[q+1]
    elif q>0:
        if c6[q]>c6[q-1]:
            x6[q]=x6[q]+x6[q-1]
print(sum(x6))
