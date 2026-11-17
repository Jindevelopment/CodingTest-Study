T = int(input())

for ts in range(1,T+1):
    num = float(input())
    temp = []
    mul = -1
    res = 0
    while num!=res:
        if len(temp)==13:
            break
        
        if num >= res+2**(mul):
            res += 2**(mul)
            temp.append(1)
        else:
        	temp.append(0)
        mul -=1
        
    print(f"#{ts}",end=" ")
    if len(temp)!=13:
    	for k in temp:
    		print(k,end="")
    	print()
    else: print("overflow")
        
    