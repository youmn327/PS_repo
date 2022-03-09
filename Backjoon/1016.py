# https://www.acmicpc.net/problem/1016 // 2.28
min_n, max_n = map(int,input().split())

eratos = [False for _ in range(max_n - min_n + 2)]

cnt = max_n - min_n + 1

i = 2
while i**2 <= max_n:
    s = min_n // (i**2)
    if min_n %(i**2) != 0:
        s += 1
    while s*(i**2) <= max_n:
        if not eratos[s*(i**2) - min_n ]:
            eratos[s*(i**2) - min_n] = True
            cnt -=1
        s+=1
    i+=1
print(cnt)
        
