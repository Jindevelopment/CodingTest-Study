# 1~10 test case
for ts in range(1,11):
    N = int(input()) # 암호문의 개수
    code = list(map(int,input().split())) # 암호문이 담긴 배열
    cmd = int(input()) # 명령어 개수
    cmd_list = list(map(str,input().split())) #명령어 담긴 배열

    # 명령어 리스트
    li = []
    for i in range(len(cmd_list)): #
        if cmd_list[i] == "I":
            for k in range(int(cmd_list[i+2])):
                code.insert(int(cmd_list[i+1])+k,int(cmd_list[i+k+3]))
        elif cmd_list[i] == "A":
            for x in range(int(cmd_list[i+1])):
                code.append(int(cmd_list[i+x+2]))
        elif cmd_list[i] == "D":
            for y in range(int(cmd_list[i+2])):
                code.pop(int(cmd_list[i+1]))

    print(f"#{ts}",end=" ")
    for z in range(10):
        print(code[z],end=" ")
    print()