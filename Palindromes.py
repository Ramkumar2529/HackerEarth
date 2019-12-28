def palin(s):
    if(s==s[::-1]):
        return True
    else:
        return False
s=input()
o=0
x=0
l=len(s)
while(x<l-1):
    a=s[:l-x]
    if(not palin(a)):
        if(len(a)>o):
            o=len(a)
    b=s[x:l]
    if(not palin(b)):
        if(len(b)>o):
            o=len(b)
    x+=1
print(o)