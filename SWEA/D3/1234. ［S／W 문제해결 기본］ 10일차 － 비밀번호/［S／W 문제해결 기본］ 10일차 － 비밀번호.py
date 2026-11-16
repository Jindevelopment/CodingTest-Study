for ts in range(1,11):
    count, num = input().split()
    count = int(count)
    num = list(num)
    
    while True:
        found = False
        
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                del num[i:i+2]
                found = True
                break
				                
        if not found:
            break
    res = "".join(num)
        
    print(f"#{ts} {res}")
    
        