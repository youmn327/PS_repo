import sys
input = sys.stdin.readline

n = int(input())
d =[-1,-1,1,-1,2,1,3,2,4,3]
for i in range(10,n+1):
    d.append(d[i-5]+1)
    
print(d[n])