T = int(input())

for ts in range(1,T+1):
    n, m = map(int,input().split())
    li1 = list(map(int,input().split()))
    li2 = list(map(int,input().split()))
    
    min_len = min(n,m)
    max_len = max(n,m)
    
    temp = []
    for i in range(max_len-min_len+1):
        total = 0
        for k in range(min_len):
            if len(li1) < len(li2):
                total += li1[k] * li2[i+k]
            else:
                total += li1[i+k] * li2[k]
        temp.append(total)
    
    print(f"#{ts} {max(temp)}")