def test(line1,line2):
    n,b=line1.split(" ")
    n,b=int(n),int(b)
    lohs=line2.split(" ")
    loh=[]
    for h in lohs:
        loh.append(int(h))
    loh.sort()
    temp=0
    c=0
    for h in loh:
        temp=temp+h
        if temp<=b:
            c=c+1
        else:
            break
    return c

res=[]
tc=int(input())
for i in range(tc):
    line1=input()
    line2=input()
    c="Case #"+str(i+1)+": "+str(test(line1,line2))
    res.append(c)

for each in res:
    print(each)
