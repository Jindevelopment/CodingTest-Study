T = int(input())

for ts in range(1,T+1):
    count = []
    li = []
    num, fly = map(int,input().split())
    for i in range(num):
        row = list(map(int,input().split()))
        li.append(row)
    
    for x in range(num-fly+1):
        for y in range(num-fly+1):
            res = 0
            for u in range(fly):
                for v in range(fly):
                    res += li[x+u][y+v]
            count.append(res)
    
    print(f"#{ts} {max(count)}")
