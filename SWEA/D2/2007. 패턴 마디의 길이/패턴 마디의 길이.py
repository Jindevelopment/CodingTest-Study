T = int(input())

for ts in range(1,T+1):
    li = input().strip()
    idx = 0
    for i in range(len(li)):
        if li[0:i+1] == li[i+1:(i+1)*2]:
            idx = i
            break
    
    print(f"#{ts} {len(li[0:idx+1])}")
