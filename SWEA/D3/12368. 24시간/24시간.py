T = int(input())

for ts in range(1,T+1):
    a, b = map(int,input().split())
    print(f"#{ts} {(a+b)%24}")