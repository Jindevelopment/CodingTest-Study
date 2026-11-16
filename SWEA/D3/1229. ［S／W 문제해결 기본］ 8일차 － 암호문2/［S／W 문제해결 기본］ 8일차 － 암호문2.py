for ts in range(1,11):
    length = int(input())
    li = list(map(int,input().split()))
    num = int(input())
    cmd = input().split()
    
    temp = []
    for i in range(len(cmd)):
        row = []
        if cmd[i] == "I":
            row.append(cmd[i])
            row.append(int(cmd[i+1]))
            row.append(int(cmd[i+2]))
            for j in range(int(cmd[i+2])):
                row.append(int(cmd[i+3+j]))
            temp.append(row)
        elif cmd[i] == "D":
            row.append(cmd[i])
            row.append(int(cmd[i+1]))
            row.append(int(cmd[i+2]))
            temp.append(row)
    
    for x in range(num):
        if temp[x][0]=="I":
            for u in range(temp[x][2]):
                li.insert(temp[x][1]+u,temp[x][u+3])
           
        elif temp[x][0] == "D":
            for z in range(temp[x][2]):
                del li[temp[x][1]]
                
            
    print(f"#{ts} ",end="")
    for w in range(10):
        print(li[w], end=" ")
    print()