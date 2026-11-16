T = int(input())

for ts in range(1,T+1):
    num = int(input())
    li = list(map(int,input().split()))
    
    ma = li[num-1]
    total = 0
    for i in range(num-2,-1,-1):
        if li[i] > ma:
            ma = li[i]
        else:
            total += ma-li[i]
            
    print(f"#{ts} {total}")