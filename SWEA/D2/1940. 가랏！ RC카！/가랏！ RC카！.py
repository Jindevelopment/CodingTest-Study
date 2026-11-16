T = int(input())

for ts in range(1,T+1):
    num = int(input())
    distance = 0
    speed = 0
    
    for i in range(num):
        li = list(map(int,input().split()))
        if li[0] == 0:
            distance += speed
        elif li[0] == 1:
            speed += li[1]
            distance += speed
        elif li[0] == 2:
            speed -= li[1]
            if speed < 0 :
                speed = 0
            distance += speed
        
    print(f"#{ts} {distance}")
        
        