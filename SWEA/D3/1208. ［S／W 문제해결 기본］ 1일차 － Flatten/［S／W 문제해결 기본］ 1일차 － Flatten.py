for ts in range(1,11):
    num = int(input())
    li = list(map(int,input().split()))
    
    for i in range(num):
        max_value = max(li)
        min_value = min(li)
        max_index = li.index(max_value)
        min_index = li.index(min_value)
        li[max_index] -= 1
        li[min_index] += 1
        
    print(f"#{ts} {max(li)-min(li)}")