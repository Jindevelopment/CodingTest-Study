T = int(input())
for ts in range(1,T+1):
    h1,m1,h2,m2 = map(int,input().split())
    res1, res2 = 0,0
    res1 = h1+h2
    res2 = m1+m2
    if res2>=60:
        res1+=res2//60
        res2%=60
    res1%=12
    if res1==0:
        res1=12
    print(f"#{ts} {res1} {res2}")
    