def solve (N,T):
    T=list(T)
    S=0
    k=T[0]
    for i in range(N):
        if(k<T[i]):
            S+=k
        else:
            k=T[i]
            S+=k
    return S
            
 
n = int(input())
T = map(int, input().split())
 
out_ = solve(n,T)
print (out_)