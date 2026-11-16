T = int(input())

for ts in range(1,T+1):
    li = list(map(int,input().split()))
    total = []
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                total.append(li[i]+li[j]+li[k])
    total = list(set(total))
    total.sort()
    
    print(f"#{ts} {total[-5]}")
    