for ts in range(1,11):
    li = []
    num = int(input())
    for i in range(num):
        rows = list(map(int,input().split()))
        li.append(rows)
    
    count = 0
    for x in range(num):
        state = 0
        for y in range(num):
            if li[y][x] == 1:
                state = 1
            elif li[y][x] == 2 and state == 1:
                state = 0
                count += 1
                
    print(f"#{ts} {count}")
            