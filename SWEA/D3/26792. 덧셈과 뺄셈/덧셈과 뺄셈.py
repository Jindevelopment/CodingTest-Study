T = int(input())

for ts in range(1,T+1):
    a, b = map(int,input().split())
    x = (a+b)//2
    y = a - x
    print(x,y)