T = int(input())

for ts in range(1,T+1):
    li = []

    for i in range(9):
        row = list(map(int,input().split()))
        li.append(row)

    #모든 행 검사
    possible = 1
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(li[i][j])
        if len(set(temp))!=9 or sum(temp) != 45:
            possible = 0
            break
        
    #모든 열 검사
    if possible == 1:
        for x in range(9):
                temp = []
                for y in range(9):
                    temp.append(li[y][x])
                if len(set(temp))!=9 or sum(temp) != 45:
                    possible = 0
                    break

    #3x3
    if possible == 1:
        for u in range(0,9,3):
            for v in range(0,9,3):
                temp = []
                for a in range(3):
                    for b in range(3):
                        temp.append(li[u+a][v+b])
                if len(set(temp))!=9 or sum(temp) != 45:
                    possible = 0
                    break

    if possible == 1:
        print(f"#{ts} 1")
    else:
        print(f"#{ts} 0")
            
