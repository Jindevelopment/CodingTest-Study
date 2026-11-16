T = int(input())
for ts in range(1,T+1):
    p,q,r,s,w = map(int,input().split())
    res1 = p*w
    if w<=r:
        res2 = q
    else:
        res2 = q+(w-r)*s
    print(f"#{ts} ",end= "")
    if res1>res2:
        print(res2)
    else:
        print(res1)