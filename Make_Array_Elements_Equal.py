
a=int(input())
ar=list(map(int,input().split()))
mc=c=0
if(len(set(ar))==1):
    print(0)
else:
    for i in range(a):
        c=0
        for j in range(i,a):
            if(ar[i]==ar[j]):
                c+=1
                if(mc<c):
                    mc=c
    print(mc)                    

