def beaseg(start,end,l2):
    middleIndex = (end - start) // 2 + start
    check = l2[start]
    for i in range(start+1,middleIndex+1):
        if (check >l2[i]):
            return 0;
        check = l2[i]
    check = l2[middleIndex]
    for i in range(middleIndex+1,end+1):
        if (check <= l2[i]):
            return 0
        check = l2[i]
    return 1
t=input()
t=int(t)
for i in range(t):
    count=0
    try:
        n=int(input())
    except ValueError:
        print(count)
        continue
    l1=list(map(int,input().strip().split()))[:n] 
    for i in range(3,n+1,2):
        start=0
        end=start+i-1
        while(end<n):
            if(beaseg(start,end,l1)):
                count+=1
            start+=1
            end+=1
    print(count)