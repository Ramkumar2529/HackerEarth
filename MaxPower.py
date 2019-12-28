import bisect
T=int(input())
for i in range(T):
    Q=int(input())
    L=[]
    for j in range(Q):
        x,y=input().split(" ")
        y=int(y)
        if(x=="P"):
            if(y>len(L)):
                print(-1)
            else:
                print(L[0-y])
        elif(x=="A"):
            bisect.insort(L,y)
        elif(x=="I"):
            L=[n+y for n in L]
        elif(x=="D"):
            L=[m-y for m in L]