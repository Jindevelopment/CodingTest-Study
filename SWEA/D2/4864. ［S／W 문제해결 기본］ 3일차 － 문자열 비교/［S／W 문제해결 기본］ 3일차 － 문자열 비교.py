T = int(input())

for ts in range(1,T+1):
    str1 = input().strip()
    str2 = input().strip()
    
    if str2.find(str1)>=0:
        print(f"#{ts} 1")
    else:
        print(f"#{ts} 0")