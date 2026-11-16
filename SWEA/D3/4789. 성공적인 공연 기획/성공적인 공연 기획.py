T = int(input())

for ts in range(1,T+1):
    st = input().strip()
    res = 0 #필요한 사람 수
    count = int(st[0]) #기립 박수를 친 사람 수
    
    for i in range(1,len(st)): 
        temp = int(st[i]) # i번째 박수 치는 사람 수\
        if count >= i: #i번째 사람이 만족 됐을 경우
            count += temp
        else: #i번째 사람이 만족되지 못해서 사람을 더 불러와야 하는 경우
            res += i-count
            count += i-count + temp
    
    print(f"#{ts} {res}")
    
            
        