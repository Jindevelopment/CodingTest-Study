for i in range(1,11):
    li = []
    repeat = int(input())
    count = 0
    
    for k in range(8):
        row = list(input())
        li.append(row)
        
    for u in range(8):
        for v in range(8-repeat+1):
            target = li[u][v:v+repeat]
            if target == target[::-1]:
                count+=1
                
    for x in range(8):
        for y in range(8-repeat+1):
            target = [row[x] for row in li[y:y+repeat]]
            if target == target[::-1]:
                count+=1
    print(f"#{i} {count}")