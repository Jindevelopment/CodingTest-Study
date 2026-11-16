T = int(input())

for ts in range(1, T + 1):
    li = []

    for i in range(9):
        rows = list(map(int, input().split()))
        li.append(rows)

    res = 1

    # 행 검사
    for k in range(9):
        temp = []

        for l in range(9):
            temp.append(li[k][l])

        if len(set(temp)) != 9:
            res = 0
            break

    # 열 검사
    if res == 1:
        for x in range(9):
            temp = []

            for y in range(9):
                temp.append(li[y][x])

            if len(set(temp)) != 9:
                res = 0
                break

    # 3×3 블록 검사
    if res == 1:
        for z in range(0, 9, 3):
            for x in range(0, 9, 3):
                temp = []

                for u in range(3):
                    for v in range(3):
                        temp.append(li[z+u][x+v])

                if len(set(temp)) != 9:
                    res = 0
                    break

            if res == 0:
                break

    print(f"#{ts} {res}")