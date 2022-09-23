# A, B,C = map(int,input().split())
# r = str(A/B)
# r = r[r.index(".")+1:]
# print(int(r[C+2]))


# f = '{'+f'{B/A}:.'+f'{C}'+'f}'
# print(f"{f}")


A,B,N = map(int, input().split())
 
for i in range(N) :
    A = (A%B)*10
    result = A//B
 
print(result)


