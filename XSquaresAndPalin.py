T=int(input())
for _ in range(T):
    S=input()
    for i in range(len(S)):
        if(S[i]!="0" and S.count(S[i])>1):
            a=S[i]
            S=S[0:i]+"0"+S[i+1:]
            x=S.index(a)
            S=S[0:x]+"0"+S[x+1:]
    l=S.count("0")
    if(l==len(S)):
        print(0)
    else:
        print(len(S)-l-1)