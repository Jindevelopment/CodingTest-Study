T = int(input())

for ts in range(1,T+1):
    num1, num2 = map(int,input().split())
    score = list(map(int,input().split()))
    score.sort()
    res = []
    for k in range(num2):
        res.append(score.pop())
    
    print(f"#{ts} {sum(res)}")