T = int(input())

for ts in range(1,T+1):
    num1, num2 = map(int,input().split())
    li = list(map(int,input().split()))
    temp = []
    
    for i in range(num1-num2+1):
        total = 0
        for j in range(i,i+num2):
            total += li[j]
        temp.append(total)
    
    print(f"#{ts} {max(temp)-min(temp)}")