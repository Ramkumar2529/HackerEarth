import bisect
def solve (a, c, M, N, X):
    for i in c:
        if(i<=X):
            bisect.insort(a,i)
    s=0
    i=0
    while(s<=X):
        s=s+a[i]
        i+=1
    return(i-1)
 
N,M,X = map(int,input().split(" "))
a=[]
for i in range(N):
    x,y=map(int,input().split(" "))
    p=y-x
    if(p<=X):
        bisect.insort(a,p)
c = list(map(int, input().split(" ")))
 
out_ = solve(a, c, M, N, X)
print (out_)