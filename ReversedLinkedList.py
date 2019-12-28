n=int(input())
l1=list(map(int,input().split()))[:n]
i=0
while(i<n):
    sl1=[]
    if(l1[i]%2==0):
        sl1.append(l1[i])
        for j in range(i+1,n):
            if(l1[j]%2==0):
                sl1.append(l1[j])
            else:
                break
        l1[i:j]=sl1[len(sl1)-1::-1]
        i=j+1
    else:
        i=i+1
if(l1[-1]%2==0):
    l1=l1[:-1]
for i in range(len(l1)):
    print(l1[i],end=" ")