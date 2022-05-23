# https://www.acmicpc.net/problem/13414

import sys
input=sys.stdin.readline
k,l=map(int,input().rstrip().split())
d=dict()
d2=dict()
lst=[]
 
for i in range(l):
    x = input().rstrip()
    d[l-i]=x 
 
d=dict(sorted(d.items()))
 
for key, val in d.items():
    d2[val] = key 
for key,val in d2.items():
    lst.append(key)
lst.reverse()
lst=lst[:k]
for i in lst:
    print(i)