T = int(input())
for ts in range(1,T+1):
    temp = int(input())
    li = list(map(int,input().split())) #입력 값
    setlist = set(li)
    res = list(sorted(setlist)) #입력 값 집합 -> 정렬
    count = [0 for i in range(len(res))] #정렬된 집합 count
    
    for i in res:
        for k in range(len(li)):
            if i == li[k]:
                count[i]+=1
    index = max(count)
    maxy_list = []
    for k in range(len(count)):
        if count[k] == index:
            maxy_list.append(res[k])
    print(f"#{ts} {max(maxy_list)}")
    