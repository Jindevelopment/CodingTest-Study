T = int(input())

for ts in range(1, T+1):
    P, A, B = map(int, input().split())

    pa, pb = 0, 0

    start_a = 1
    start_b = 1
    end_a = P
    end_b = P

    while start_a <= end_a:
        middle_a = (start_a + end_a) // 2
        pa += 1

        if middle_a == A:
            break
        elif middle_a > A:
            end_a = middle_a
        else:
            start_a = middle_a

    while start_b <= end_b:
        middle_b = (start_b + end_b) // 2
        pb += 1

        if middle_b == B:
            break
        elif middle_b > B:
            end_b = middle_b
        else:
            start_b = middle_b

    if pa < pb:
        print(f"#{ts} A")
    elif pa > pb:
        print(f"#{ts} B")
    else:
        print(f"#{ts} 0")