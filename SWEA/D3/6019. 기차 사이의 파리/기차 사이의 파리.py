T = int(input())

for ts in range(1,T+1):
    D, A, B, F = map(int,input().split())
    res = D/(A+B) * F
    print(f"#{ts} {res:.6f}")
    