T = int(input())

for ts in range(1,T+1):
    num = int(input())
    li = input().split()
    res1 = []
    res2= []
    res=[]
    if num%2==0:
        for u in range(num//2):
            res1.append(li[u])
        for p in range(num//2,num):
            res2.append(li[p])
    else:
        for v in range(num//2):
            res1.append(li[v])
        for q in range(num//2+1,num):
            res2.append(li[q])
        res1.append(li[num//2])
    
    if num%2 ==0:
        for k in range(num//2):
            res.append(res1[k])
            res.append(res2[k])
    else:
        for x in range(num//2):
            res.append(res1[x])
            res.append(res2[x])
        res.append(res1[-1])
            
    print(f"#{ts} ",end="")
    for j in res:
        print(j,end=" ")
    print()