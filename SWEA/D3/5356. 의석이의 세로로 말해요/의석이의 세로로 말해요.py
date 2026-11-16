T = int(input())

for ts in range(1,T+1):
    li = []
    
    for k in range(5):
        row = list(input().strip())
        li.append(row)
    
    max_len = 0
    for j in range(5):
        if max_len < len(li[j]):
            max_len=len(li[j])
    
    res = ""
    for x in range(max_len):
        for y in range(5):
            if x < len(li[y]):
                res += li[y][x]
                
    print(f"#{ts} {res}")
                
                