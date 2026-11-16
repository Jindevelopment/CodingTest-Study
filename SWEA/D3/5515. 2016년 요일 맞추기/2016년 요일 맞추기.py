T = int(input())

month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for ts in range(1,T+1):
    m, d = map(int, input().split())
    temp = 4
    if m == 1:
        d -= 1
        temp += d
    else: 
        for i in range(1,m):
            temp += month[i]
        temp += d-1
    
    print(f"#{ts} {temp%7}")