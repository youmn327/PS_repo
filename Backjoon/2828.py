from sys import stdin


n, m = map(int, stdin.readline().split())
j = int(stdin.readline())

p_list = []
distance = 0

for _ in range(j):
    p = int(stdin.readline())
    p_list.append(p)

    if (value := max(p_list) - min(p_list) - m) >= 0:
        distance += (value + 1)

        if p == max(p_list):
            p_list = [p - m + 1, p]
        else:
            p_list = [p + m - 1, p]

print(distance)