from collections import Counter

N = int(input())
lst = sorted(list(map(int,input().split())))
M = int(input())
se_lst = list(map(int,input().split()))

wcount = Counter(lst)
for i in se_lst:
    print(wcount[i],end=" ")