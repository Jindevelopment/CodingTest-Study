T = int(input())

for ts in range(1, T + 1):
    num = int(input())
    li = []

    for i in range(num):
        li.append(list(map(int, input().strip())))

    start = (num - 1) // 2
    total = 0

    for x in range(start + 1):
        total += sum(li[x][start-x:start+x+1])

    for y in range(start + 1, num):
        total += sum(li[y][y-start:num-(y-start)])

    print(f"#{ts} {total}")