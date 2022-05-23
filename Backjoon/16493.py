# https://www.acmicpc.net/problem/16493 , 미완료
import sys

N, M = map(int,input().split())

lst = [tuple(map(int,input().split())) for i in range(N)]

print(lst)
return_book = []
for i in range(len(lst)):
    max_count = 0
    for j in range(i,len(lst)):
        if i == j :
            continue
        max_count += lst[j][i]

        if max_count == M :
            return_book.append()
