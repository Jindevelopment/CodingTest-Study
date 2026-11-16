for ts in range(1,11):
    length = int(input())
    li = list(map(int,input().split()))
    num = int(input())
    cmd = list(input().split())
    
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

        elif cmd[i] == "A":
            row.append(cmd[i])
            row.append(int(cmd[i+1]))
            for k in range(int(cmd[i+1])):
                row.append(int(cmd[i+2+k]))
            temp.append(row)
        
    for x in range(num):
        if temp[x][0]=="I":
            for y in range(temp[x][2]):
                li.insert(temp[x][1]+y,temp[x][3+y])
  
        elif temp[x][0] == "D":
            for u in range(temp[x][2]):
                del li[temp[x][1]]

        elif temp[x][0] == "A":
            for v in range(temp[x][1]):
                li.append(temp[x][2+v])
                       
                       

    print(f"#{ts} ",end="")
    for z in range(10):
        print(li[z],end=" ")
    print()
            
                
        