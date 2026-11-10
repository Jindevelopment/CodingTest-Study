for ts in range(1,11):
    st = int(input())
    li = []
    for p in range(100):
        row = list(map(int,input().split()))
        li.append(row)
        
    res = []
    
    #행의 합
    for i in range(100):
        sum = 0
        for k in range(100):
            sum += li[i][k]
        res.append(sum)
    
    #열의 합
    for x in range(100):
        sum = 0
        for y in range(100):
            sum += li[y][x]
        res.append(sum)
    
    #오른쪽 아래 대각선의 합
    right_sum = 0
    for u in range(100):
        for v in range(100):
            if u==v:
                right_sum+=li[u][v]
    res.append(right_sum)
    
    #왼쪽 아래 대각선의 합
    left_sum = 0
    for q in range(100):
        left_sum += li[q][99-q]
    res.append(left_sum)
    
    print(f"#{ts} {max(res)}")