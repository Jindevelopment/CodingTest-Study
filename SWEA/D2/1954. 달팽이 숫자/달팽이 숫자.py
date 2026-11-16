T = int(input())

for ts in range(1,T+1):
    i, j, cnt = 0, 0, 1

    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    dr = 0
    N = int(input())
    arr = [ [0] * N for i in range(N)]
    arr[i][j] = cnt
    cnt += 1
    while cnt <= N*N:
        ni = i + di[dr]
        nj = j + dj[dr]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr+1) % 4
        
    print(f"#{ts}")
    for k in arr:
        print(*k)