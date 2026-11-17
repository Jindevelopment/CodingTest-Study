T = int(input())

for ts in range(1,T+1):
    num = int(input())
    
    li = list(map(int,input().split()))
    print(f"#{ts} {max(li)-min(li)}")