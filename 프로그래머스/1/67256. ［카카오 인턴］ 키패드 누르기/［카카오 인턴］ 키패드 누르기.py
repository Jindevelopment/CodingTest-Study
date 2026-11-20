def solution(numbers, hand):
    answer = ''
    
    li = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left_x, left_y = 3,0
    right_x, right_y = 3,2
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            if i == 1:
                left_x = 0
            elif i == 4:
                left_x = 1
            elif i == 7:
                left_x = 2
            left_y = 0
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            if i == 3:
                right_x = 0
            elif i == 6:
                right_x = 1
            elif i == 9:
                right_x = 2
            right_y = 2
        elif i==2 or i == 5 or i == 8 or i == 0:
            find_x = 0
            find_y = 0
            # 2,5,8,0의 위치 찾기
            for x in range(4):
                for y in range(3):
                    if li[x][y] == i:
                        find_x = x
                        find_y = y
            
            d_l = abs(find_x-left_x) + abs(find_y-left_y) #왼손과의 거리
            d_r = abs(find_x-right_x) + abs(find_y-right_y) #오른손과의 거리
            
            if d_l == d_r:
                if hand == "left":
                    left_x = find_x
                    left_y = find_y
                    answer += "L"
                elif hand == "right" :
                    right_x = find_x
                    right_y = find_y
                    answer+="R"
            elif d_l < d_r:
                answer += "L"
                left_x = find_x
                left_y = find_y
            else:
                answer += "R"
                right_x = find_x
                right_y = find_y
    
    return answer

