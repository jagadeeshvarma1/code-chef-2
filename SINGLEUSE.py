t = int(input())
for _ in range(t):
    h, x, y = map(int, input().split())
    if h <= x:
        print(1)
    else:
        num_regular_attacks = (h - y + x - 1) // x
        if h - num_regular_attacks * x <= y:
            print(num_regular_attacks + 1)
        else:
            print(num_regular_attacks + 2)