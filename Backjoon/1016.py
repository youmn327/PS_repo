# https://www.acmicpc.net/problem/1016 // 2.28
min, max = map(int,input().split())
cnt = 0
result = False
for i in range(min,max+1):
    for j in range(2,i):
        if i % j **2 != 0 and i < 10:
            cnt += 1
            break
        

        

            
            
print(1000,cnt)