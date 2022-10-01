def ring(n):
    names = [input() for _ in range(n)]
    ring_names = {}
    for _ in range(2 * n - 1):
        a, b = list(map(str, input().split()))
        # 인덱스 + 1(a)을 key로 입력 받아 1로 초기화
        # 중복되는 key가 나오면 +1를 해서 2로
        ring_names[a] = ring_names.get(a, 0) + 1

    # 귀걸이를 돌려받은 학생은 value = 2
    # 돌려받지 못한 학생은 value = 1
    for key, val in ring_names.items():
        if val == 1:
            return names[int(key) - 1]


ans = []
cnt = 1
while True:
    n = int(input())
    if n == 0: break
    print(cnt, ring(n))
    cnt += 1