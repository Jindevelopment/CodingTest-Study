def solution(rows, columns, queries):
    answer = [] #뽑은 것들 중 가장 작은 숫자 리스트
    use = [] #각 회전에서 만진 숫자 리스트
    arr = [[0] * columns for _ in range(rows)] #초기 배열 생성
    start = 1
    #1. 배열 초기값 생성
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = start
            start+=1
    
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    dr = 0
    
    for x in queries:
        start_x = x[0]-1
        end_x = x[2]-1
        start_y = x[1]-1
        end_y = x[3]-1
        much = (x[2]-x[0]+1)*(x[3]-x[1]+1) - (x[2]-x[0]-1)*(x[3]-x[1]-1)  # 10
        cnt = 0
        i,j = start_x, start_y
        prev = arr[i][j]
        sl = []
        
        
        while cnt < much:
            ni, nj = i + di[dr], j + dj[dr]
            
            if start_x<=ni<=end_x and start_y<=nj<=end_y:
                sl.append(prev)
                temp = arr[ni][nj]
                arr[ni][nj] = prev
                prev = temp
                i,j = ni,nj
                cnt+=1
            else:
                dr = (dr+1)%4
        
        use.append(sl)
            
            
    for q in use:
        answer.append(min(q))
            
    return answer