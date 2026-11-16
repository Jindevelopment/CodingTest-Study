T = int(input())

for ts in range(1,T+1):
    num = int(input())
    res = ""
    for i in range(num):
        a,b = input().split()
        b = int(b)
        res += a*b
    
    print(f"#{ts}")
    for x in range(len(res)//10+1):
        print(res[x*10:x*10+10])
	
        