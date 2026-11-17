T = int(input())

for ts in range(1,T+1):
    li = input().strip().split()
    stack = []
    for i in li:
        if i != "*" and i != "/" and i != "-" and i != "+" and i != ".":
            stack.append(int(i))
        else:
            if i == ".":
                if len(stack) == 1:
                	print(f"#{ts} {stack[0]}")
                else:
                	print(f"#{ts} error")
                	break
            elif len(stack)>=2 and type(stack[-1])==int and type(stack[-2]) == int:
                a = stack.pop()
                b = stack.pop()
                if i == "*":
                    stack.append(a*b)
                elif i == "/":
                    if a == 0:
                        print(f"#{ts} error")
                        break
                    else:
                    	stack.append(b//a)
                elif i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(b-a)
            else:
                print(f"#{ts} error")
                break
                    