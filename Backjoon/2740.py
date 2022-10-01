n, m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]


m, k = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(m)]

answer = [[0 for _ in range(k)] for _ in range(n)]
print(answer)

for n in range(n):
    for k in range(k):
        for m in range(m):
            answer[n][k] += A[n][m] * B[m][k]
    
print(A,B)
print(answer)


def matrix_f():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    M, K = map(int, input().split())
    B = []
    for _ in range(M):
        B.append(list(map(int, input().split())))



    C = [[0 for _ in range(K)] for _ in range(N)]
    print(A,B)
    for n in range(N):
        for k in range(K):
            for m in range(M):
                C[n][k] += A[n][m] * B[m][k]
    return C

# C = matrix_f()


for i in answer:
    for j in i:
        print(j, end = ' ')
    print()