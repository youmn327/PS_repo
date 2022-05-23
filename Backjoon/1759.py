# https://www.acmicpc.net/problem/1759  미완성
from itertools import combinations

N, M = map(int,input().split())

word_lst = sorted(input().split())
result = [''.join(i) for i in list(combinations(word_lst,N))]
for i in result:
    if "a" in i:
        print(i)
    elif "e" in i:
        print(i)
    elif "i" in i:
        print(i)
    elif "o" in i:
        print(i)
    elif "u" in i:
        print(i)
    else:
        pass