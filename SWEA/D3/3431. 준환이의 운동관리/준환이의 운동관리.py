T = int(input())

for ts in range(1,T+1):
    L, U, X = map(int,input().split()) #1주일에 L분 이상 U분 이하의 운동 , 실제 운동 : X
    res = 0
    if X>U:
        res = -1
    elif X<=L:
        res = L-X
    
    print(f"#{ts} {res}")
    
    