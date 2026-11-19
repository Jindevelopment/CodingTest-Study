T = int(input())

for ts in range(1,T+1):
    print(f"#{ts}")
    
    num = int(input())
    li = [[0] * num for _ in range(num)]
    cnt = 1
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    i, j, dr = 0, 0, 0
    li[0][0]=cnt
    
    while cnt < num*num:
        ni, nj = i+di[dr], j + dj[dr]
        if 0<=ni<num and 0<=nj<num and li[ni][nj]==0:
            cnt +=1
            li[ni][nj] = cnt
            i, j = ni, nj
        else:
            dr = (dr+1)%4
    
    for x in range(num):
        for y in range(num):
            print(li[x][y], end = " ")
        print()
        