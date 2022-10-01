# https://www.acmicpc.net/problem/2018

n = int(input())
if n%2 == 0 :
    lst = [i for i in range(1,(n//2)+1)]
else:
    lst = [i for i in range(1,((n//2)+1)+1)]

left, right = 0, 1
cnt = 1
while right <= len(lst):
    total  = sum(lst[left:right])
    if total == n:
        cnt += 1
        left += 1
        right = left+1
    elif total < n:
        right += 1
    else:
        left += 1
        right = left+1
print(cnt)

# 바보 였다.. 등차수열 문제를...