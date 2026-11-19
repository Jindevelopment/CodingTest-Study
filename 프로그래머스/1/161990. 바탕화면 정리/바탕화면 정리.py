def solution(wallpaper):
    answer = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                temp = [i,j]
                answer.append(temp)
    
    li_x = []
    li_y = []
    for x in answer:
        li_x.append(x[0])
        li_y.append(x[1])
        
    res = [min(li_x),min(li_y),max(li_x)+1,max(li_y)+1]
    return res